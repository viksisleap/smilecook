"""empty message

Revision ID: d5bba62919dc
Revises: 67f54df8952c
Create Date: 2021-01-05 23:57:14.110121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5bba62919dc'
down_revision = '67f54df8952c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###
