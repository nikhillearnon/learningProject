"""Create projects table

Revision ID: 5a7dc3a09abc
Revises: 6099300c10d7
Create Date: 2025-09-17 22:27:56.466595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '5a7dc3a09abc'
down_revision: Union[str, Sequence[str], None] = '6099300c10d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('title', sa.String(length=255), unique=True, index=True, nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('deadline', sa.DateTime(), nullable=True, default=datetime.now),
        sa.Column('created_at', sa.DateTime(), nullable=True, default=datetime.now),
    )


def downgrade() -> None:
    op.drop_table('projects')
