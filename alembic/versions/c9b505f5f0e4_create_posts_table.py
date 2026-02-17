"""create posts table

Revision ID: c9b505f5f0e4
Revises: 67bbb0ca9ec8
Create Date: 2026-02-16 15:26:41.015882

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c9b505f5f0e4"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
    "posts",
    sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
    sa.Column("title", sa.String(), nullable=False),
    )

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts") 
    pass
