from contextlib import contextmanager
from src.database.database import Database
from src.database.database_commons import Session


# interfaces the Database class in order to wrap it
class DatabaseInterface:
    @contextmanager
    def __get_session_commit(self):
        session = Session()
        yield session
        session.commit()
        session.close()

    def __init__(self, database_config, logger):
        self.__database = Database(database_config)
        self.__logger = logger

    # ==== channels ====

    def get_channel_instruction(self, channel_id):
        with self.__get_session_commit() as session:
            channel = self.__database.get_channel_instruction(session, channel_id)
            if channel is not None:
                session.expunge(channel)
            return channel

    def set_channel_instruction(self, channel_id, channel_instruction):
        self.__logger.info("set the following instructions : '" + channel_instruction + "' for the channel " + str(channel_id))
        with self.__get_session_commit() as session:
            self.__database.get_or_create_channel_instruction(session, channel_id, channel_instruction)

    def remove_channel_instruction(self, channel_id):
        self.__logger.info("removed all instructions for the channel " + str(channel_id))
        with self.__get_session_commit() as session:
            self.__database.remove_channel_instruction(session, channel_id)

    # trusted roles

    def get_trusted_roles(self, discord_guild_id):
        with self.__get_session_commit() as session:
            roles = self.__database.get_trusted_roles_discord(session, discord_guild_id)
            for role in roles:
                if role is not None:
                    session.expunge(role)
            return roles

    def set_trusted_roles(self, discord_guild_id, trusted_roles_list):
        self.__logger.info("added the following trusted roles for the discord " + str(discord_guild_id) + " : " + ", ".join(str(x.id) + " / " + str(x.name) for x in trusted_roles_list))
        with self.__get_session_commit() as session:
            for trusted_role in trusted_roles_list:
                self.__database.get_or_create_trusted_role(session, discord_guild_id, trusted_role.id, trusted_role.name)

    def remove_trusted_roles(self, discord_guild_id, trusted_roles_list):
        self.__logger.info("removed all trusted roles for the channel " + str(discord_guild_id))
        with self.__get_session_commit() as session:
            for trusted_role in trusted_roles_list:
                self.__database.remove_one_trusted_role(session, trusted_role)
