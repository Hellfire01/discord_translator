from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class DiscordGuildModel(Base):
    __tablename__ = 'discord_guild'
    id = Column(Integer, primary_key=True)
    guild_discord_id = Column(String)

