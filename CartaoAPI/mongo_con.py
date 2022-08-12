from pymongo import MongoClient

# Casa Standlone
# client = MongoClient('mongodb://localhost:27017/',
#                      username='root',
#                      password='example')
# Casa docker-compose
client = MongoClient('mongodb://mongo:27017/',
                     username='root',
                     password='root_pwd')

db = client.clientes
collection = db.cartoes
collection2 = db.clientes
