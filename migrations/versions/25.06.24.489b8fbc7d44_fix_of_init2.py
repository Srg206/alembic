"""fix_of_init2

Revision ID: 489b8fbc7d44
Revises: 86d2c787c47b
Create Date: 2024-06-25 14:13:42.037196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489b8fbc7d44'
down_revision = '86d2c787c47b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('msg_chat')
    op.drop_table('msg_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('msg_user',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('msg_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['msg_id'], ['message.id'], name='msg_user_msg_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='msg_user_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'msg_id', name='msg_user_pkey')
    )
    op.create_table('msg_chat',
    sa.Column('chat_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('msg_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], name='msg_chat_chat_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['msg_id'], ['message.id'], name='msg_chat_msg_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('chat_id', 'msg_id', name='msg_chat_pkey')
    )
    # ### end Alembic commands ###
