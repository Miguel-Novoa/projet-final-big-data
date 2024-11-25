"""Update User migration

Revision ID: 98f2fc5fa8f2
Revises: 97640f915130
Create Date: 2024-11-25 21:59:47.515528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98f2fc5fa8f2'
down_revision: Union[str, None] = '97640f915130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=False))
    op.drop_index('ix_users_pseudo', table_name='users')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_column('users', 'pseudo')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pseudo', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_index('ix_users_pseudo', 'users', ['pseudo'], unique=True)
    op.drop_column('users', 'username')
    # ### end Alembic commands ###