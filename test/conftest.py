import pytest
# from passlib.context import CryptContext
from config.db import get_db


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
