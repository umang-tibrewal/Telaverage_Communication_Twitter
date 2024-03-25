"""Initial migration.

Revision ID: 0865c2d9d665
Revises: 
Create Date: 2024-03-25 01:07:17.330584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0865c2d9d665'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweetsearchresult',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('query_key', sa.String(), nullable=True),
    sa.Column('no_of_likes', sa.Integer(), nullable=True),
    sa.Column('no_of_retweets', sa.Integer(), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('tweet_text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweetsearchresult')
    # ### end Alembic commands ###
