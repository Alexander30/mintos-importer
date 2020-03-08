"""create mintos_statements table

Revision ID: b18f0478ba29
Revises: b7a70396a181
Create Date: 2020-02-15 15:27:30.746040

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b18f0478ba29'
down_revision = 'b7a70396a181'
branch_labels = None
depends_on = None

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


def upgrade():
  op.create_table(
    'p2p_lending_platforms_mintos_statements',
    sa.Column('id', sa.INTEGER, primary_key=True, nullable=False),
    sa.Column('investment_account_id', sa.INTEGER, primary_key=True, nullable=False),
    sa.Column('statement_file', sa.dialects.postgresql.BYTEA, nullable=False),
    sa.Column('statement_file_type', filetypes, nullable=False),
    sa.Column('upload_timestamp', sa.TIMESTAMP, nullable=False),
    sa.Column('document_sha256_hash', sa.CHAR(64), unique=True, nullable=False),
    sa.Column('transactions_total', sa.INTEGER, nullable=False),
    sa.Column('first_transaction_timestamp', sa.TIMESTAMP, nullable=False),
    sa.Column('last_transaction_timestamp', sa.TIMESTAMP, nullable=False),
    sa.Column('processing_state', statement_processing_states, nullable=False),
    sa.Column('processing_start_timestamp', sa.TIMESTAMP),
    sa.Column('processing_finish_timestamo', sa.TIMESTAMP)
  )


def downgrade():
  op.drop_table('p2p_lending_platforms_mintos_statements')
  statement_processing_states.drop(op.get_bind())
  filetypes.drop(op.get_bind())
