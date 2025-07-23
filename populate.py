from database import engine, SessionLocal
from models import Base, Offer

Base.metadata.create_all(bind=engine)

db = SessionLocal()

offers = [
    Offer(bank="HDFC", card_type="Credit", min_order_amount=5000, discount_amount=500),
    Offer(bank="HDFC", card_type="Debit", min_order_amount=3000, discount_amount=200),
    Offer(bank="SBI", card_type="Credit", min_order_amount=4000, discount_amount=400),
    Offer(bank="ICICI", card_type="Credit", min_order_amount=4500, discount_amount=300),
]

db.add_all(offers)
db.commit()
db.close()

print("Test offers inserted into offers.db ✅")
