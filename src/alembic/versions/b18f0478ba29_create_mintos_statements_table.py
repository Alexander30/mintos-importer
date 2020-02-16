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
  statement_processing_states = sa.dialects.postgresql.ENUM(
    'new',
    'processing',
    'processed',
    'failed',
    name='statement_processing_state'
  )

  filetypes = sa.dialects.postgresql.ENUM(
    'xlsx',
    name='filetypes'
  )

  op.create_table(
    'mintos_statements',
    sa.Column('id', sa.INTEGER, primary_key=True),
    sa.Column('investment_account_id', sa.INTEGER, primary_key=True),
    sa.Column('statement_file', sa.dialects.postgresql.BYTEA),
    sa.Column('statement_file_type', filetypes),
    sa.Column('upload_timestamp', sa.TIMESTAMP),
    sa.Column('document_sha256_hash', sa.CHAR(64), unique=True),
    sa.Column('transactions_total', sa.INTEGER),
    sa.Column('first_transaction_timestamp', sa.TIMESTAMP),
    sa.Column('last_transaction_timestamp', sa.TIMESTAMP),
    sa.Column('processing_state', statement_processing_states),
    sa.Column('processing_start_timestamp', sa.TIMESTAMP),
    sa.Column('processing_finish_timestamo', sa.TIMESTAMP)
  )


def downgrade():
  op.drop_table('mintos_statements')