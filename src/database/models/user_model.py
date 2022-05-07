from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_discord_id = Column(String)
