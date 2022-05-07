from sqlalchemy import Column, Integer, String
from src.database.database_commons import Base


class LangModel(Base):
    __tablename__ = 'lang'
    id = Column(Integer, primary_key=True)
    emote = Column(String)
    name = Column(String)
