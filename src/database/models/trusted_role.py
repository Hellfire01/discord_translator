from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class TrustedRoleModel(Base):
    __tablename__ = 'discord_guild'
    id = Column(Integer, primary_key=True)
    role_discord_id = Column(String)
