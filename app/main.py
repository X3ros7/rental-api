from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, SessionLocal, engine
from app.routers import auth, properties, tenants
from app.seed import seed_demo_data


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_demo_data(db)
    finally:
        db.close()
    yield


app = FastAPI(title="RentAI API", version="1.0.0", lifespan=lifespan)

app.include_router(auth.router)
app.include_router(properties.router)
app.include_router(tenants.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
