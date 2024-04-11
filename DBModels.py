from sqlalchemy import Column, Integer, String
from DBconnection import Base
class Desserts(Base):

    __tablename__ = "desserts"
    dessert_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    dessert_type = Column(String)
    price = Column(Integer)
    time = Column(Integer)
class Salads(Base):

    __tablename__ = "salads"
    salads_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    salad_type = Column(String)
    portion = Column(Integer)
    availability = Column(String)
    additional = Column(String)
    price = Column(Integer)
    time = Column(Integer)