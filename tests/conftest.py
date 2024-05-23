"""configuration of context"""
import pytest
from src.app import create_app


# Configura la aplicación Flask para pruebas
app = create_app()


@pytest.fixture
def client():
    """create client"""
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client_app:
        with app.app_context():
            yield client_app
