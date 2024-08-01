"""change cpf column

Revision ID: ea10c426a4d8
Revises: b5107b7d74ee
Create Date: 2024-07-29 20:13:20.444482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea10c426a4d8'
down_revision: Union[str, None] = 'b5107b7d74ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transactional_data', 'cpf',
               existing_type=sa.VARCHAR(length=11),
               type_=sa.String(length=25),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transactional_data', 'cpf',
               existing_type=sa.String(length=25),
               type_=sa.VARCHAR(length=11),
               existing_nullable=True)
    # ### end Alembic commands ###