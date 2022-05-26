from src.database.models.channel_model import ChannelModel
from src.database.models.trusted_role import TrustedRoleModel
from src.database.models.discord_guild import DiscordGuildModel
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

    # === roles ===

    # === discord guild ===
    # note :
    # this section has no removal yet
    # removal would need a check that there are no longer any attached allowed roles

    def get_discord_guild(self, session, discord_guild_id):
        instance = session.query(DiscordGuildModel).filter_by(guild_discord_id=discord_guild_id).first()
        return instance

    def create_discord_guild(self, session, discord_guild_id):
        discord_guild = self.get_discord_guild(session, discord_guild_id)
        if discord_guild is None:
            discord_guild = DiscordGuildModel(guild_discord_id=discord_guild_id)
            session.add(discord_guild)
