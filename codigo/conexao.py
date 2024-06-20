from pymongo import MongoClient

# Configuração do cliente MongoDB
client = MongoClient('localhost', 27017)
db = client['biblioteca']
colecao = db['livros']
