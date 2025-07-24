from pydantic import BaseModel
from datetime import datetime

class WorkerStatusCreate(BaseModel):
    worker_id: str
    heart_rate: int
    start_time: datetime

class FactoryStatusResponse(BaseModel):
    production_count: int
    defect_rate: float
    status: str
    last_updated: datetime
