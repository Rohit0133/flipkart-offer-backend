from sqlalchemy.orm import Session
from schemas import OfferRequest, OfferResponse
from models import Offer

def get_best_offer(payload: OfferRequest, db: Session) -> OfferResponse:
    matching_offers = db.query(Offer).filter(
        Offer.bank.ilike(payload.bank),
        Offer.card_type.ilike(payload.card_type),
        Offer.min_order_amount <= payload.order_amount
    ).all()

    if not matching_offers:
        return OfferResponse(
            bank=payload.bank,
            card_type=payload.card_type,
            discount_amount=0.0
        )

    best = max(matching_offers, key=lambda offer: offer.discount_amount)

    return OfferResponse(
        bank=best.bank,
        card_type=best.card_type,
        discount_amount=best.discount_amount
    )
