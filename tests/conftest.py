"""configuration of context"""
import os
import pytest
import psycopg2
from src.taxis import app


@pytest.fixture
def client():
    """to create client"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client_app:
        with app.app_context():
            yield client_app


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
