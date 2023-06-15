"""Remove nullable

Revision ID: 671a9bddfc58
Revises: 9b32bfe36460
Create Date: 2023-06-15 14:24:57.773549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '671a9bddfc58'
down_revision = '9b32bfe36460'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
