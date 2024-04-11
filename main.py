from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from DBconnection import SessionLocal, engine
from typing import Dict, List
import DBModels, Schemas
import uvicorn

DBModels.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_DB():
    DB = SessionLocal()
    try:
        yield DB
    finally:
        DB.close()
        
@app.post('/create_desserts', response_model=None, status_code=201)
async def create_desserts(item:Schemas.Desserts, DB:Session=Depends(get_DB)):
    DB_item = DBModels.Desserts(name=item.name, description=item.description, dessert_type=item.dessert_type,
                                price=item.price,                                time=item.time)
    DB.add(DB_item)
    DB.commit()
    DB.refresh(DB_item)

@app.post('/create_salads', response_model=None, status_code=201)
async def create_salads(item: Schemas.Salads, DB:Session=Depends(get_DB)):
    DB_item = DBModels.Salads(name=item.name, description=item.description, salad_type=item.salad_type,
                                price=item.price, portion=item.portion, availability=item.availability,                                additional=item.additional, time=item.time)
    DB.add(DB_item)
    DB.commit()
    DB.refresh(DB_item)

@app.get('/desserts',  response_model=List[Schemas.Desserts])
async def get_desserts(DB:Session=Depends(get_DB)):
    return DB.query(DBModels.Desserts).all()

@app.get('/salads',  response_model=List[Schemas.Salads])
async def get_salads(DB:Session=Depends(get_DB)):
    return DB.query(DBModels.Salads).all()

@app.put('/update_desserts/{dessert_id}', response_model=None, status_code=200)
async def update_desserts(dessert_id: int, item: Schemas.Desserts, DB:Session=Depends(get_DB), new_args: Dict=None):
    cls_name = DBModels.Desserts
    DB_item = DB.query(cls_name).filter(cls_name.dessert_id == dessert_id).first()
    if DB_item:
        for key, val in new_args.items():
            setattr(DB_item, key, val)
        DB.commit()
        DB.refresh(DB_item)

@app.put('/update_salads/{salads_id}', response_model=None, status_code=200)
async def update_salads(salads_id: int, item: Schemas.Desserts, DB:Session=Depends(get_DB),new_args: Dict=None):
    cls_name = DBModels.Salads
    DB_item = DB.query(cls_name).filter(cls_name.salads_id == salads_id).first()
    if DB_item:
        for key, val in new_args.items():
            setattr(DB_item, key, val)
        DB.commit()
        DB.refresh(DB_item)

@app.delete('/delete_desserts/{dessert_id}', response_model=None, status_code=204)
async def delete_desserts(dessert_id: int, item:Schemas.Desserts, DB:Session=Depends(get_DB)):
    cls_name = DBModels.Desserts
    DB_item = DB.query(cls_name).filter(cls_name.dessert_id == dessert_id).first()
    if DB_item:
        DB.delete(DB_item)
        DB.commit()

@app.delete('/delete_salads/{salads_id}', response_model=None, status_code=204)
async def delete_salads(salads_id: int, item:Schemas.Desserts, DB:Session=Depends(get_DB)):
    cls_name = DBModels.Desserts
    DB_item = DB.query(cls_name).filter(cls_name.salads_id == salads_id).first()
    if DB_item:
        DB.delete(DB_item)
        DB.commit()


if __name__ == 'main':
    uvicorn.run('main:app', reload=True)
