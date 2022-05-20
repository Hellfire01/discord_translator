from contextlib import contextmanager
from src.database.database_commons import Session
from src.database.database import Database


# interfaces the Database class in order to wrap it
class DatabaseInterface:
    @contextmanager
    def __get_session(self):
        session = Session()
        yield session
        session.commit()
        session.close()

    def __init__(self):
        self.database = Database()

    def get_user(self, user_id):
        with self.__get_session() as session:
            self.database.get_user(user_id, session)

    def create_user(self, user_id):
        with self.__get_session() as session:
            self.database.create_user(user_id, session)

    def set_user_channel_combo(self, user, channel, lang_in, lang_out):
        with self.__get_session() as session:
            pass
