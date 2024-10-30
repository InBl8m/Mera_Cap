from sqlalchemy.orm import Session
from .models import Price


def create_price(db: Session, ticker: str, price: float, timestamp: int):
    db_price = Price(ticker=ticker, price=price, timestamp=timestamp)
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price


def get_prices_by_ticker(db: Session, ticker: str):
    return db.query(Price).filter(Price.ticker == ticker).all()


def get_latest_price_by_ticker(db: Session, ticker: str):
    return db.query(Price).filter(Price.ticker == ticker).order_by(Price.timestamp.desc()).first()


def get_prices_by_date_range(db: Session, ticker: str, date_from: int, date_to: int):
    return db.query(Price).filter(
        Price.ticker == ticker,
        Price.timestamp >= date_from,
        Price.timestamp <= date_to
    ).all()
