import backend.crud as crud  # noqa: PLR0402
import pytest
import pytest_asyncio
from backend.config import settings
from backend.database import Base
from backend.main import app, get_db
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from backend import (
    models,  # noqa: F401  # Ensure model tables are registered in Base.metadata.
)


@pytest_asyncio.fixture
async def engine():
    """Create DB engine"""
    engine = create_async_engine(settings.DATABASE_URL, echo=False, poolclass=NullPool)
    yield engine
    await engine.dispose()

@pytest_asyncio.fixture
async def setup_db(engine):
    """Create tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
    # Cleanup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture
async def db(engine, setup_db, monkeypatch):
    """
        Session BD for each test
    """
    session_factory  = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    monkeypatch.setattr(crud, "SessionLocal", session_factory)
    async with session_factory() as session:
        yield session

@pytest.fixture
def client(db):
    """
        Client test
    """
    async def override_get_db():
        yield db
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
