from sqlalchemy import Column, Integer, String, Float
from database import Base

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    bank = Column(String, index=True)
    card_type = Column(String, index=True)
    min_order_amount = Column(Float)
    discount_amount = Column(Float)
