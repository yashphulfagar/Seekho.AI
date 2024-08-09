import json
import pytest
from app import app

@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def runner():
    from flask.cli import FlaskGroup
    cli = FlaskGroup(app)
    yield cli

