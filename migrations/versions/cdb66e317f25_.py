"""empty message

Revision ID: cdb66e317f25
Revises: e1d3e2159e74
Create Date: 2021-12-10 15:09:29.340333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdb66e317f25'
down_revision = 'e1d3e2159e74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cloth', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('img', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cloth', schema=None) as batch_op:
        batch_op.drop_column('img')
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
