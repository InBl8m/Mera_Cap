import ssl
import aiohttp
from time import time
from sqlalchemy.orm import Session
from .models import Price
from .database import SessionLocal


async def fetch_price(session, currency):
    url = f"https://www.deribit.com/api/v2/public/get_index_price?index_name={currency}"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with session.get(url, ssl=ssl_context) as response:
        data = await response.json()
        return data['result']['index_price'], int(time())


async def fetch_and_store():
    async with aiohttp.ClientSession() as session:
        currencies = ['btc_usd', 'eth_usd']

        db: Session = SessionLocal()
        for currency in currencies:
            price, timestamp = await fetch_price(session, currency)
            db_price = Price(ticker=currency, price=price, timestamp=timestamp)
            db.add(db_price)

        db.commit()
        db.close()
