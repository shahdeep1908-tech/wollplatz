"""empty message

Revision ID: 7d30ed2c35df
Revises: 35b144c25d56
Create Date: 2022-07-28 13:20:13.534181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d30ed2c35df'
down_revision = '35b144c25d56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('selectors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('website_id', sa.Integer(), nullable=True),
    sa.Column('title_selector', sa.String(), nullable=True),
    sa.Column('price_selector', sa.String(), nullable=True),
    sa.Column('composition_selector', sa.String(), nullable=True),
    sa.Column('needle_size_selector', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['website_id'], ['website_url.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_selectors_id'), 'selectors', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_selectors_id'), table_name='selectors')
    op.drop_table('selectors')
    # ### end Alembic commands ###