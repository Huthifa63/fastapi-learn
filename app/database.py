import psycopg2
import time
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# ✅ Prefer DATABASE_URL on Render (works best with Render Postgres)
# Falls back to the old separate env vars if DATABASE_URL isn't set.
if getattr(settings, "database_url", None):
    SQLALCHEMY_DATABASE_URL = settings.database_url
else:
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{settings.database_username}:"
        f"{settings.database_password}@"
        f"{settings.database_hostname}:"
        f"{settings.database_port}/"
        f"{settings.database_name}"
    )

engine = create_engine(str(SQLALCHEMY_DATABASE_URL))

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------
# Database Connection (Postgres) - psycopg2
# ----------------------------
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="postgres123",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connection to database failed:", error)
#         time.sleep(2)
