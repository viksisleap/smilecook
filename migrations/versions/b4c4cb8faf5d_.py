"""empty message

Revision ID: b4c4cb8faf5d
Revises: df19cdd82cc7
Create Date: 2021-01-08 13:39:05.488768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4c4cb8faf5d'
down_revision = 'df19cdd82cc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('ingredients', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipe', 'ingredients')
    # ### end Alembic commands ###
