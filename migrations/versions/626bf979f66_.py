"""Creating `users` table

Revision ID: 626bf979f66
Revises: None
Create Date: 2014-11-01 06:33:16.502777

"""

# revision identifiers, used by Alembic.
revision = '626bf979f66'
down_revision = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=140), nullable=False),
        sa.Column('password', sa.String(length=40), nullable=False), # sha1
        sa.Column('salt', sa.String(length=40), nullable=False), # sha1
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade():
    op.drop_table('users')
