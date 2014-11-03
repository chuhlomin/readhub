"""Creating `users` table

Revision ID: 626bf979f66
Revises: None
Create Date: 2014-11-01 06:33:16.502777

"""

# revision identifiers, used by Alembic.
revision = '626bf979f66'
down_revision = None

from alembic import op
import sqlalchemy as db


def upgrade():
    op.create_table(
        'users',
        db.Column('id', db.Integer, primary_key=True, nullable=False, autoincrement=True),
        db.Column('email', db.String(length=140), nullable=True),  # <--
        db.Column('password', db.String(length=40), nullable=True),  # sha1
        db.Column('salt', db.String(length=40), nullable=False),  # sha1
        db.UniqueConstraint('email'),
    )


def downgrade():
    op.drop_table('users')
