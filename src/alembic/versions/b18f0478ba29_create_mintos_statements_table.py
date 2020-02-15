"""create mintos_statements table

Revision ID: b18f0478ba29
Revises: 
Create Date: 2020-02-15 15:27:30.746040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18f0478ba29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
    'mintos_statements',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('investment_account_id', sa.Integer, primary_key=True),
    sa.Column('upload_date_time', sa.DateTime)
  )


def downgrade():
  op.drop_table('mintos_statements')