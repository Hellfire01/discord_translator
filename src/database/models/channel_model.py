from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class ChannelModel(Base):
    __tablename__ = 'channel'
    id = Column(Integer, primary_key=True)
    channel_discord_id = Column(String)
    # this string references the desired output languages as one string separated by '/' such as "fr/eng" or "du/sp/ru"
    lang_string_instruction = Column(String)
