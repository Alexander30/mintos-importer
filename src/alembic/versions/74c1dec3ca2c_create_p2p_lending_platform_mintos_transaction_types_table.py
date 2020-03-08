"""create p2p_lending_platform_mintos_transaction_types table

Revision ID: 74c1dec3ca2c
Revises: b18f0478ba29
Create Date: 2020-02-17 03:02:32.089929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74c1dec3ca2c'
down_revision = 'b18f0478ba29'
branch_labels = None
depends_on = None


def upgrade():
  mintos_transaction_types = op.create_table(
    'p2p_lending_platform_mintos_transaction_types',
    sa.Column('id', sa.INTEGER, primary_key=True, nullable=False),
    sa.Column('name', sa.String, unique=True, nullable=False)
  )

  op.bulk_insert(mintos_transaction_types,
    [
      {'name': 'Deposits'},
      {'name': 'Withdrawals'},
      {'name': 'Withdrawal cancelled'},
      {'name': 'Cashback bonus'},
      {'name': 'Refer a friend bonus'},
      {'name': 'Outgoing currency exchange transaction'},
      {'name': 'Incoming currency exchange transaction'},
      {'name': 'FX commission'},
      {'name': 'Investment in loan'},
      {'name': 'Investment in loan  - Invest & Access'},
      {'name': 'Loan payment: principal received'},
      {'name': 'Loan payment: interest received'},
      {'name': 'Loan agreement amended: principal received'},
      {'name': 'Loan agreement amended: interest received'},
      {'name': 'Loan early repayment: principal received'},
      {'name': 'Loan early repayment: interest received'},
      {'name': 'Loan agreement terminated: principal received'},
      {'name': 'Loan agreement terminated: interest received'},
      {'name': 'Loan buyback: principal received'},
      {'name': 'Loan buyback: interest received'},
      {'name': 'Loan buyback: late payment interest received'},
      {'name': 'Loan agreement extended: principal received'},
      {'name': 'Loan agreement extended: interest received'},
      {'name': 'Loan late fees received'},
      {'name': 'Other: principal received'},
      {'name': 'Other: interest received'},
      {'name': 'Other: late payment interest received'},
      {'name': 'Secondary market transaction'},
      {'name': 'Secondary market transaction  - Invest & Access'},
      {'name': 'Discount for secondary market transaction'},
      {'name': 'Premium for secondary market transaction'},
      {'name': 'Cumulative repurchases of loan parts'},
    ]
  )


def downgrade():
  op.drop_table('p2p_lending_platform_mintos_transaction_types')
