from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas
from .database import get_db

router = APIRouter()


@router.get("/prices", response_model=List[schemas.Price])
def get_all_prices(ticker: str = Query(...), db: Session = Depends(get_db)):
    prices = crud.get_prices_by_ticker(db, ticker)
    if not prices:
        raise HTTPException(status_code=404, detail="Prices not found")

    return prices


@router.get("/prices/latest", response_model=schemas.Price)
def get_latest_price(ticker: str = Query(...), db: Session = Depends(get_db)):
    price = crud.get_latest_price_by_ticker(db, ticker)
    if price:
        return price
    else:
        raise HTTPException(status_code=404, detail="Price not found")


@router.get("/prices/by_date", response_model=List[schemas.Price])
def get_price_by_date(
    ticker: str = Query(...),
    date_from: int = Query(...),
    date_to: int = Query(...),
    db: Session = Depends(get_db)
):
    prices = crud.get_prices_by_date_range(db, ticker, date_from, date_to)
    if not prices:
        raise HTTPException(status_code=404, detail="Prices not found in the specified date range")
    return prices
