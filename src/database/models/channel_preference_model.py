from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class ChannelPreferenceModel(Base):
    __tablename__ = 'channel_preference'
    id = Column(Integer, primary_key=True)
