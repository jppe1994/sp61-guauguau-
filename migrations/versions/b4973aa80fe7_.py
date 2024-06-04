"""empty message

Revision ID: b4973aa80fe7
Revises: a7a1e2dd66e6
Create Date: 2024-06-04 21:15:21.279489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4973aa80fe7'
down_revision = 'a7a1e2dd66e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('owner', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'city', ['city_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('owner', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('city_id')

    # ### end Alembic commands ###
