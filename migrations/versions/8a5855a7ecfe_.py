"""empty message

Revision ID: 8a5855a7ecfe
Revises: 2cf36d9d4dcb
Create Date: 2022-05-10 00:57:14.935752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a5855a7ecfe'
down_revision = '2cf36d9d4dcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('length', sa.String(length=120), nullable=False),
    sa.Column('width', sa.String(length=120), nullable=False),
    sa.Column('passengers', sa.String(length=120), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###