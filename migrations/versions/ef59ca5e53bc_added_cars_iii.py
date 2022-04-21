"""added cars III

Revision ID: ef59ca5e53bc
Revises: 5ce0ea7b6f08
Create Date: 2022-04-20 18:27:56.001696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef59ca5e53bc'
down_revision = '5ce0ea7b6f08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('color', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('car', 'color')
    # ### end Alembic commands ###
