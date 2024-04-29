import pytest
from src.main import app
import psycopg2
import os


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope="module")
def db_connection():
    """Fixture para establecer la conexión a la base de datos."""
    connection = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DATABASE'),
        port=5432
    )
    yield connection
    connection.close()
