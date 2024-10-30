import os
from pymongo import MongoClient
from pymongo.database import Database


def get_db() -> Database:
    '''
        Obtém a instância do banco de dados apropriada (produção ou testes)
        baseada no ambiente.
    '''
    env = os.getenv('ENV', 'prod')
    client = MongoClient("mongodb://localhost:27017/")
    db_name = "test_db" if env == "test" else "prod_db"
    return client[db_name]
