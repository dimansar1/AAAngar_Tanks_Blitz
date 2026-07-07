from fastapi import FastAPI

from app.api.health import router as health_router
from app.config.config import get_settings
from app.schemas.tanks import TankCreate, TankResponce

settings = get_settings()

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    debug = settings.debug,
)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
    }

@app.post("/tanks", response_model = TankResponce)
def create_tank(tank: TankCreate):
    return {
        "id": 1,
        "title": tank.title,
        #TODO: photo
        "health": tank.health,
        "damage": tank.damage,
        "armor": tank.armor,
        "history": tank.history,
        "recommendation": tank.recommendation,
        "category": tank.category,
        "nation": tank.nation,
        "level": tank.level,
    }




# title: str
#     #TODO: photo
#     health: str
#     damage: str
#     armor: str
#     history: str
#     recommendation: str
#     category: str
#     nation: str
#     level: str