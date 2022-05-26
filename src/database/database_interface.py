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

    def __init__(self, database_config):
        self.__database = Database(database_config)

    # ==== channels ====

    def get_channel_instruction(self, channel_id):
        with self.__get_session_commit() as session:
            channel = self.__database.get_channel_instruction(session, channel_id)
            if channel is not None:
                session.expunge(channel)
            return channel

    def set_channel_instruction(self, channel_id, channel_instruction):
        with self.__get_session_commit() as session:
            self.__database.create_channel_instruction(session, channel_id, channel_instruction)

    def remove_channel_instruction(self, channel_id):
        with self.__get_session_commit() as session:
            self.__database.remove_channel_instruction(session, channel_id)

