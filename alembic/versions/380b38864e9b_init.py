"""init

Revision ID: 380b38864e9b
Revises: 
Create Date: 2022-08-29 10:21:56.719939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '380b38864e9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('env',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=255), nullable=False),
    sa.Column('client_secret', sa.String(length=255), nullable=False),
    sa.Column('api_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_url'),
    sa.UniqueConstraint('client_id')
    )
    op.create_index(op.f('ix_env_id'), 'env', ['id'], unique=False)
    op.create_table('feed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.String(length=255), nullable=False),
    sa.Column('company_scrape_id', sa.String(length=255), nullable=False),
    sa.Column('feed_id', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feed_id'), 'feed', ['id'], unique=False)
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_table('envfeed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feed_id', sa.Integer(), nullable=True),
    sa.Column('env_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['env_id'], ['env.id'], ),
    sa.ForeignKeyConstraint(['feed_id'], ['feed.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_envfeed_id'), 'envfeed', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_envfeed_id'), table_name='envfeed')
    op.drop_table('envfeed')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_feed_id'), table_name='feed')
    op.drop_table('feed')
    op.drop_index(op.f('ix_env_id'), table_name='env')
    op.drop_table('env')
    # ### end Alembic commands ###
