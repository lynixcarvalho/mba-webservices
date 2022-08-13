from pymongo import MongoClient


client = MongoClient('mongodb://mongo:27017/',
                     username='root',
                     password='root_pwd')

db = client.clientes
collection = db.cartoes
collection2 = db.clientes
