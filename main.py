from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import OfferRequest, OfferResponse
from logic import get_best_offer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working 🎉"}

@app.post("/offer", response_model=OfferResponse)
def calculate_offer(payload: OfferRequest, db: Session = Depends(get_db)):
    best_offer = get_best_offer(payload, db)
    return best_offer


