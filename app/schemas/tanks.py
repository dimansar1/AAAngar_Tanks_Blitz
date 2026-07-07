from pydantic import BaseModel

class TankCreate(BaseModel):
    title: str
    #TODO: photo
    health: str
    damage: str
    armor: str
    history: str
    recommendation: str
    category: str
    nation: str
    level: str

class TankResponce(BaseModel):
    id: int
    title: str
    #TODO: photo
    health: str
    damage: str
    armor: str
    history: str
    recommendation: str
    category: str
    nation: str
    level: str
