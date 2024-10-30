import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.client import fetch_and_store
from app import models
from app.database import engine
from app.api import router as api_router


models.Base.metadata.create_all(bind=engine)
app = FastAPI(lifespan=lambda app: lifespan(app))
app.include_router(api_router)


async def periodic_fetch():
    while True:
        await fetch_and_store()
        await asyncio.sleep(60)


@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch_task = asyncio.create_task(periodic_fetch())
    yield
    fetch_task.cancel()
    await fetch_task


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
