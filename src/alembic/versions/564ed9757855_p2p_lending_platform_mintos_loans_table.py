"""create p2p_lending_platform_mintos_loans table

Revision ID: 564ed9757855
Revises: 74c1dec3ca2c
Create Date: 2020-03-08 08:10:41.163349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '564ed9757855'
down_revision = '74c1dec3ca2c'
branch_labels = None
depends_on = None

p2p_lending_platform_mintos_loan_type = sa.dialects.postgresql.ENUM(
  'Agricultural Loan',
  'Business Loan',
  'Car Loan',
  'Forward Flow Loan',
  'Invoice Financing',
  'Mortgage Loan',
  'Pawnbroking Loan',
  'Personal Loan',
  'Short-Term Loan'
  name='p2p_lending_platform_mintos_loan_type'
)

def upgrade():
  op.create_table(
    'p2p_lending_platform_mintos_loans',
    sa.Column('id', sa.INTEGER, primary_key=True, nullable=False),
    sa.Column('mintos_loan_id', sa.String, unique=True, nullable=False)
    sa.Column('mintos_loan_type', p2p_lending_platform_mintos_loan_type, nullable=True)
  )

def downgrade():
  op.drop_table('p2p_lending_platform_mintos_statements')
  p2p_lending_platform_mintos_loan_type.drop(op.get_bind())
