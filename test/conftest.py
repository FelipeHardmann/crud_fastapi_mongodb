import pytest
from config.db import get_db
from models.user import User as UserModel


@pytest.fixture(scope='function')
def db_session():
    '''
        Fixture que fornece uma sessão de banco
        de dados limpa para cada teste.
    '''
    db = get_db()

    for colletion_name in db.list_collection_names():
        db[colletion_name].delete_many({})

    yield db

    for colletion_name in db.list_collection_names():
        db[colletion_name].delete_many({})


@pytest.fixture(scope='function')
def user_on_db(db_session):
    user = UserModel(
        name='Felipe',
        email='felipe@email.com',
        password='Felipe123#'
    )

    user_dict = user.model_dump()
    user_id = db_session['user'].insert_one(user_dict).inserted_id

    yield user

    db_session['user'].delete_one({'_id': user_id})
