from jose import JWTError, jwt
from datetime import datetime, timedelta

from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .config import settings
from . import schemas, database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# ✅ clean values (this fixes HS256 issues caused by quotes/spaces/newlines)
SECRET_KEY = (settings.secret_key or "").strip()  # type: ignore
ALGORITHM = (settings.algorithm or "").strip().upper()  # type: ignore
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes  # type: ignore

# ✅ fail fast if env is wrong
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is empty/missing")
if not ALGORITHM:
    raise RuntimeError("ALGORITHM is empty/missing")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    try:
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except Exception as e:
        # clearer error in Render logs
        raise RuntimeError(f"JWT encode failed (algorithm={ALGORITHM}): {e}")


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=int(user_id))

    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    if user is None:
        raise credentials_exception

    return user
