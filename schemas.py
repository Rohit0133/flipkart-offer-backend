from pydantic import BaseModel

class OfferRequest(BaseModel):
    bank: str
    card_type: str
    order_amount: float

class OfferResponse(BaseModel):
    bank: str
    card_type: str
    discount_amount: float

