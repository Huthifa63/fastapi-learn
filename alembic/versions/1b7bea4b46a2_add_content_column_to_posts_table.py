"""add content column to posts table

Revision ID: 1b7bea4b46a2
Revises: c9b505f5f0e4
Create Date: 2026-02-16 15:36:59.508341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b7bea4b46a2'
down_revision: Union[str, Sequence[str], None] = 'c9b505f5f0e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass
    """Upgrade schema."""
    


def downgrade() -> None:
    op.drop_column("posts", "content")
    """Downgrade schema."""
    pass
