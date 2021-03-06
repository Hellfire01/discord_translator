from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.database_commons import Base


class TrustedRoleModel(Base):
    __tablename__ = 'trusted_role'
    id = Column(Integer, primary_key=True)
    role_discord_id = Column(Integer)
    role_name = Column(String)
    discord_guild_id = Column(Integer, ForeignKey('discord_guild.guild_discord_id'))
    discord_guild = relationship("DiscordGuildModel", backref="trusted_roles")
