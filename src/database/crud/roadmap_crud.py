from sqlalchemy.orm import Session
from src.models import RoadmapModel
from src.schemas import RoadmapSchema
from uuid import UUID, uuid4

def get_roadmap(db: Session, roadmap_id: UUID):
    return db.query(RoadmapModel).filter(RoadmapModel.id_roadmap == roadmap_id).first()

def create_roadmap(db: Session, roadmap: RoadmapSchema):
    id_roadmap = uuid4()
    db_roadmap = RoadmapModel(
        id_roadmap=id_roadmap,
        title=roadmap.title,
        description=roadmap.description,
        price=roadmap.price,
        places=roadmap.places,
        images=roadmap.images,
    )
    db.add(db_roadmap)
    db.commit()
    db.refresh(db_roadmap)
    return db_roadmap

def get_roadmap_by_id(db: Session, email: str):
    return db.query(RoadmapModel).filter(RoadmapModel.email == email).first()
