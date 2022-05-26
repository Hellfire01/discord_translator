from src.database.models.channel_model import ChannelModel
from src.database.models.trusted_role_model import TrustedRoleModel
from src.database.models.discord_guild_model import DiscordGuildModel
from src.database.database_commons import Base, Engine


class Database:
    def __init__(self, database_config):
        self.database_config = database_config
        Base.metadata.create_all(Engine)

    # ==== channels ====

    def get_channel_instruction(self, session, channel_id):
        instance = session.query(ChannelModel).filter_by(channel_discord_id=channel_id).first()
        return instance

    def get_or_create_channel_instruction(self, session, channel_id, instructions):
        channel = self.get_channel_instruction(session, channel_id)
        if channel is None:
            channel = ChannelModel(channel_discord_id=channel_id, lang_string_instruction=instructions)
            session.add(channel)
        else:
            channel.lang_string_instruction = instructions
        return channel

    def remove_channel_instruction(self, session, channel_id):
        session.query(ChannelModel).filter_by(channel_discord_id=channel_id).delete()

    def get_channel_instructions(self, session):
        return session.query(ChannelModel).all()

    # === roles ===

    def get_trusted_role(self, session, trusted_role_id):
        instance = session.query(TrustedRoleModel).filter_by(role_discord_id=trusted_role_id).first()
        return instance

    def get_trusted_roles_discord(self, session, discord_guild_id):
        instance = session.query(TrustedRoleModel).filter_by(discord_guild_id=discord_guild_id).all()
        return instance

    def get_or_create_trusted_role(self, session, discord_guild_id, trusted_role_id, trusted_role_name):
        trusted_role = self.get_trusted_role(session, trusted_role_id)
        if trusted_role is None:
            discord_guild = self.get_or_create_discord_guild(session, discord_guild_id)
            print(trusted_role_id)
            trusted_role = TrustedRoleModel(role_discord_id=trusted_role_id, discord_guild=discord_guild, role_name=trusted_role_name)
            session.add(trusted_role)

    def remove_one_trusted_role(self, session, trusted_role_id):
        session.query(TrustedRoleModel).filter_by(role_discord_id=trusted_role_id).delete()

    # === discord guild ===
    # note :
    # this section has no removal yet
    # removal would require a check that there are no longer any attached allowed roles

    def get_discord_guild(self, session, discord_guild_id):
        instance = session.query(DiscordGuildModel).filter_by(guild_discord_id=discord_guild_id).first()
        return instance

    def get_or_create_discord_guild(self, session, discord_guild_id):
        discord_guild = self.get_discord_guild(session, discord_guild_id)
        if discord_guild is None:
            discord_guild = DiscordGuildModel(guild_discord_id=discord_guild_id)
            session.add(discord_guild)
        return discord_guild
