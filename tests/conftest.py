"""configuration of context"""
import pytest
from src.app import create_app

# Configura la aplicación Flask para pruebas
app = create_app()


@pytest.fixture
def client():
    """create client"""
    # app.register_blueprint(taxis)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client_app:
        with app.app_context():
            yield client_app
