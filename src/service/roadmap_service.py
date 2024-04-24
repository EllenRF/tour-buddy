from src.schemas.roadmap_schema import RoadmapSchema
from src.database.crud import roadmap_crud
from src.database.db import get_db

class RoadmapService():
    def __init__(self):
        self.db = get_db()

    def create_roadmap(self, roadmap: RoadmapSchema):
        try:
            db_roadmap = roadmap_crud.create_roadmap(self.db, roadmap=roadmap)
        except Exception as e:
            raise e
        
        return db_roadmap.id_roadmap