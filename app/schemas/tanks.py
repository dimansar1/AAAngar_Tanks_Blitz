from pydantic import BaseModel

class TankCreate(BaseModel):
    title: str
    photo_path: str
    health: str
    damage: str
    armor: str
    history: str
    recommendation: str
    category: str
    nation: str
    level: str

class TankResponse(BaseModel):
    id: int
    title: str
    photo_path: str
    health: str
    damage: str
    armor: str
    history: str
    recommendation: str
    category: str
    nation: str
    level: str
