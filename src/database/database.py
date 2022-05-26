from src.database.models.channel_model import ChannelModel
from src.database.database_commons import Base, Engine


class Database:
    def __init__(self, database_config):
        self.database_config = database_config
        Base.metadata.create_all(Engine)

    # ==== channels ====

    def get_channel_instruction(self, session, channel_id):
        instance = session.query(ChannelModel).filter_by(channel_discord_id=channel_id).first()
        return instance

    def create_channel_instruction(self, session, channel_id, instructions):
        channel = self.get_channel_instruction(session, channel_id)
        if channel is None:
            channel = ChannelModel(channel_discord_id=channel_id, lang_string_instruction=instructions)
            session.add(channel)
        else:
            channel.lang_string_instruction = instructions

    def remove_channel_instruction(self, session, channel_id):
        session.query(ChannelModel).filter_by(channel_discord_id=channel_id).delete()

    def get_channel_instructions(self, session):
        return session.query(ChannelModel).all()
