from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class ChannelModel(Base):
    __tablename__ = 'channel'
    id = Column(Integer, primary_key=True)
    channel_discord_id = Column(String)
