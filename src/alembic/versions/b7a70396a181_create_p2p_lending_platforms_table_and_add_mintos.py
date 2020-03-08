"""create p2p_lending_platforms table and/or mintos entry

Revision ID: b7a70396a181
Revises:
Create Date: 2020-02-17 00:52:02.194262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7a70396a181'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  conn = op.get_bind()
  inspector = sa.engine.reflection.Inspector.from_engine(conn)
  tables = inspector.get_table_names()
  table_name = 'p2p_lending_platforms'

  if table_name not in tables:
    p2p_lending_platforms = op.create_table(
      table_name,
      sa.Column('id', sa.INTEGER, primary_key=True, nullable=False),
      sa.Column('name', sa.String, unique=True, nullable=False)
    )
  else:
    meta = sa.MetaData(conn)
    meta.reflect(only=(table_name,))
    p2p_lending_platforms = sa.Table(table_name, meta)
    meta = sa.MetaData(conn)
    meta.reflect(only=(table_name,))
    p2p_lending_platforms = sa.Table(table_name, meta)

  op.bulk_insert(p2p_lending_platforms,
    [
      {'name': 'mintos'}
    ]
  )


def downgrade():
  op.get_bind().execute(sa.sql.text("DELETE FROM p2p_lending_platforms WHERE name = 'mintos';"))
