import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from app.db.database import Base, get_session
from app.core.config import get_settings
from main import app

settings = get_settings()

TEST_DATABASE_URL = settings.DATABASE_URL


@pytest.fixture(scope="session")
def setup_db():
    if settings.MODE == "TEST":
        engine = create_engine(TEST_DATABASE_URL)
        session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        connection = engine.connect()
        transaction = connection.begin()
        session = session_maker(bind=connection)
        yield session

        session.close()
        transaction.rollback()
        connection.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_session():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
