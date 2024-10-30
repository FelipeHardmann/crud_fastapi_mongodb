from fastapi.testclient import TestClient
from main import app
from fastapi import status
from models.user import User

client = TestClient(app)


def test_add_user_route(db_session):
    body = {
        "name": "Felipe",
        "email": "felipe@email.com",
        "password": "Felipe#1234"
    }

    response = client.post('/register', json=body)

    assert response.status_code == status.HTTP_201_CREATED
    user_on_db = db_session['user'].find_one({'email': body['email']})

    assert user_on_db is not None
    assert user_on_db['name'] == body['name']
    assert user_on_db['email'] == body['email']

    db_session['user'].delete_one({'email': body['email']})
