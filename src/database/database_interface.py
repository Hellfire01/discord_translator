from src.database.database import Database


# interfaces the Database class in order to wrap it
class DatabaseInterface:
    def __init__(self):
        self.database = Database()

    def get_user(self, user_id):
        self.database.get_user(user_id)

    def create_user(self, user_id):
        self.database.create_user(user_id)

    def get_user_channel_combo(self, user, channel):
        pass

    def set_user_channel_combo(self, user, channel, lang_in, lang_out):
        pass


# todo :
# help => indicate a usage example more detailed ( something that could be copy / pasted )
# use case where nothing to be translated was given => give dedicated error message
