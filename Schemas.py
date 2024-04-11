from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    name: str
    description: str
    price: int
    time: int

    class Config:
        orm_mode = True

class Desserts(Item):
    dessert_type:str

class Salads(Item):
    salad_type: str
    portion: int
    availability: str
    additional: str