from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductionData(Base):
    __tablename__ = 'production_data'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    total_steam = Column(Float)
    finishing = Column(Float)
    weaving = Column(Float)
    recombing = Column(Float)
    grey_combing = Column(Float)
    dyeing = Column(Float)
    spinning = Column(Float)
    sludge_drier = Column(Float)
    ws = Column(Float)
    pc_dyg = Column(Float)
    tfo = Column(Float)
    steaming_mc = Column(Float)
    unmetered = Column(Float)
    unmetered_percentage = Column(Float)
    dm_water = Column(Float)
    recovery_percentage = Column(Float)
