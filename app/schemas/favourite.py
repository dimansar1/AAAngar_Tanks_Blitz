from pydantic import BaseModel, ConfigDict

class FavouriteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    tank_id: int
    user_id: int