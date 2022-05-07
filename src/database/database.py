from src.database.models.user_model import UserModel
from src.database.models.lang_model import LangModel
from src.database.models.channel_model import ChannelModel
from src.database.models.user_preference_model import UserPreferenceModel
from src.database.database_commons import Base, Session, Engine


class Database:
    def __init__(self):
        Base.metadata.create_all(Engine)

    def get_user_list(self):
        return []

    def get_user(self, discord_id):
        session = Session()
        instance = session.query(UserModel).filter_by(user_discord_id=discord_id).first()
        session.close()
        return instance

    def create_user(self, discord_id):
        if self.get_user(discord_id) is None:
            session = Session()
            user = UserModel(user_discord_id=discord_id)
            session.add(user)
            session.commit()
            session.close()

    def get_channels(self):
        return []

    def get_channel(self, channel_model):
        return None

    def get_langs(self):
        return []

    def get_lang(self, lang_model):
        return None

    def get_user_preferences(self):
        return []

    def get_user_preference(self, user_model, channel_model):
        return None
