"""defining embedded_chunk table

Revision ID: e2d33755acdc
Revises: ed10ab340d5f
Create Date: 2023-10-26 13:05:59.003745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import pgvector  # type: ignore


# revision identifiers, used by Alembic.
revision: str = "e2d33755acdc"
down_revision: Union[str, None] = "ed10ab340d5f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.create_table(
        "embedded_chunk",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("file_upload_id", sa.Integer(), nullable=False),
        sa.Column("chunk_index", sa.Integer(), nullable=False),
        sa.Column("vector", pgvector.sqlalchemy.Vector(dim=1536), nullable=False),
        sa.Index(
            "vector_hnsw_idx",
            "vector",
            postgresql_using="hnsw",
            postgresql_with={"m": 16, "ef_construction": 64},
            postgresql_ops={"vector": "vector_cosine_ops"},
        ),
        sa.ForeignKeyConstraint(
            ["file_upload_id"],
            ["file_upload.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("embedded_chunk")
    # ### end Alembic commands ###
