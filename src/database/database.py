from src.database.models.user_model import UserModel
from src.database.models.channel_model import ChannelModel
from src.database.database_commons import Base, Engine


class Database:
    def __init__(self, database_config):
        self.database_config = database_config
        Base.metadata.create_all(Engine)

    # ==== users ====

    def get_user_list(self):
        return []

    def get_user(self, session, discord_id):
        instance = session.query(UserModel).filter_by(user_discord_id=discord_id).first()
        return instance

    def create_user(self, session, discord_id):
        if self.get_user(discord_id, session) is None:
            user = UserModel(user_discord_id=discord_id)
            session.add(user)

    # ==== channels ====

    def get_channel_instruction(self, session, channel_id):
        instance = session.query(ChannelModel).filter_by(channel_discord_id=channel_id).first()
        return instance

    def create_channel_instruction(self, session, channel_id, instructions):
        channel = self.get_channel_instruction(channel_id, session)
        if channel is None:
            channel = ChannelModel(channel_discord_id=channel_id, lang_string_instruction=instructions)
            session.add(channel)
        else:
            channel.lang_string_instruction = instructions

    def get_channel_instructions(self, session):
        return session.query(ChannelModel).all()
