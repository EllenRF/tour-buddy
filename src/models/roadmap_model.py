from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from src.database.db import engine
from src.database import Base
from .user_model import UserModel

class RoadmapModel(Base):
    __tablename__ = "roadmap"

    id_roadmap = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey(UserModel.id_user), primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    images = Column(ARRAY(String), nullable=True)