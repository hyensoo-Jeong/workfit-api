from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class WorkerStatus(Base):
    __tablename__ = "worker_status"

    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(String, index=True)
    heart_rate = Column(Integer)
    start_time = Column(DateTime, default=datetime.utcnow)

class FactoryStatus(Base):
    __tablename__ = "factory_status"

    id = Column(Integer, primary_key=True, index=True)
    production_count = Column(Integer)
    defect_rate = Column(Float)
    status = Column(String)  # operating, stopped, error
    last_updated = Column(DateTime, default=datetime.utcnow)
