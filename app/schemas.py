from pydantic import BaseModel


class PriceBase(BaseModel):
    ticker: str
    price: float
    timestamp: int


class Price(PriceBase):
    id: int

    class Config:
        from_attributes = True
