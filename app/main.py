"""@package app.main
@brief Entry point of the RentAI FastAPI application.

Creates the ASGI app, registers routers, and initializes the database
with demo data on startup.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, SessionLocal, engine
from app.routers import auth, properties, tenants
from app.seed import seed_demo_data


@asynccontextmanager
async def lifespan(_: FastAPI):
    """@brief Application lifespan hook.

    Creates database tables and seeds demo data before the API starts
    serving requests.

    @param _ FastAPI application instance (unused).
    """
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
    """@brief Health-check endpoint.

    @return Dictionary with service status, e.g. ``{"status": "ok"}``.
    """
    return {"status": "ok"}
