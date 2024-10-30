from sqlalchemy import Column, String, Float, Integer
from .database import Base


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)
