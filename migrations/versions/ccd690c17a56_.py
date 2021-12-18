"""empty message

Revision ID: ccd690c17a56
Revises: 5157ebd15c73
Create Date: 2021-12-18 11:30:08.723047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd690c17a56'
down_revision = '5157ebd15c73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('address', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('detail_address', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('detail_address')
        batch_op.drop_column('address')
        batch_op.drop_column('name')

    # ### end Alembic commands ###