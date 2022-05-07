from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.database.database_commons import Base


lang_user_preferences = Table("lang_user_preference",
                              Base.metadata,
                              Column('lang_id', Integer, ForeignKey('lang.id')),
                              Column('user_preference_id', Integer, ForeignKey('user_preferences.id'))
                              )


class UserPreferenceModel(Base):
    __tablename__ = 'user_preferences'
    id = Column(Integer, primary_key=True)
    input_lang_id = Column(Integer, ForeignKey("lang.id"))
    input_lang = relationship("LangModel")
    output_langs = relationship("LangModel",
                                secondary=lang_user_preferences,
                                )
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("UserModel")
    channel_id = Column(Integer, ForeignKey("channel.id"))
    channel = relationship("ChannelModel")
