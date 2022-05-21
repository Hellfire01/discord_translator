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

    def get_user(self, user_id):
        with self.__get_session_commit() as session:
            user = self.__database.get_user(user_id, session)
            session.expunge(user)
            return user

    def create_user(self, user_id):
        with self.__get_session_commit() as session:
            self.__database.create_user(user_id, session)

    def get_channel_instruction(self, channel_id):
        with self.__get_session_commit() as session:
            channel = self.__database.get_channel_instruction(session, channel_id)
            session.expunge(channel)
            return channel

    def set_channel_instruction(self, channel_id, channel_instruction):
        with self.__get_session_commit() as session:
            self.__database.create_channel_instruction(session, channel_id, channel_instruction)

