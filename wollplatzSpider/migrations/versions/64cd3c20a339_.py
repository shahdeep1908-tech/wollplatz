"""empty message

Revision ID: 64cd3c20a339
Revises: b0a4acbf5a08
Create Date: 2022-08-02 11:58:25.084604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64cd3c20a339'
down_revision = 'b0a4acbf5a08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('website_url',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('links', sa.String(), nullable=True),
    sa.Column('pattern', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('brands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('website_id', sa.Integer(), nullable=True),
    sa.Column('brand_selector', sa.String(), nullable=True),
    sa.Column('linking_url', sa.String(), nullable=True),
    sa.Column('brand_name', sa.String(), nullable=True),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['website_id'], ['website_url.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_brands_id'), 'brands', ['id'], unique=False)
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
    op.drop_index(op.f('ix_brands_id'), table_name='brands')
    op.drop_table('brands')
    op.drop_table('website_url')
    # ### end Alembic commands ###
