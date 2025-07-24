from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, WorkerStatus, FactoryStatus
from schemas import WorkerStatusCreate, FactoryStatusResponse
from fastapi import FastAPI
from fcm import send_fcm_notification
from pydantic import BaseModel

app = FastAPI()
Base.metadata.create_all(bind=engine)

# 입력 형식 정의
class AlertRequest(BaseModel):
    device_token: str
    title: str
    body: str

# DB 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello from WorkFit API"}

@app.get("/factory-status", response_model=FactoryStatusResponse)
def get_factory_status(db: Session = Depends(get_db)):
    latest = db.query(FactoryStatus).order_by(FactoryStatus.id.desc()).first()
    return latest

@app.post("/worker-status")
def post_worker_status(data: WorkerStatusCreate, db: Session = Depends(get_db)):
    new_status = WorkerStatus(**data.dict())
    db.add(new_status)
    db.commit()
    db.refresh(new_status)
    return {"message": "Worker status saved"}

@app.post("/raise-alert")
def raise_alert(alert: AlertRequest):
    status, result = send_fcm_notification(
        device_token=alert.device_token,
        title=alert.title,
        body=alert.body
    )
    return {
        "status": status,
        "firebase_response": result
    }