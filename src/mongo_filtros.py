# src/mongo_filtros.py: praticando find() e operadores
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pymongo import MongoClient
from config import MONGO_URL

cliente = MongoClient(MONGO_URL)
colecao = cliente["pipeline_cambio"]["pessoas_teste"]

# Fase A: limpar antes de inserir (idempotência - já vamos testar isso)
colecao.delete_many({})

# Fase B: inserir vários documentos - reparem no 3o, com um campo A MAIS
colecao.insert_many([
    {"nome": "Ana", "cidade": "Recife", "idade": 25},
    {"nome": "Bruno", "cidade": "Recife", "idade": 32},
    {"nome": "Carla", "cidade": "Olinda", "idade": 28, "bolsista": True},
])

# Fase C: filtros
print("--- Pessoas do Recife ---")
for pessoa in colecao.find({"cidade": "Recife"}):
    print(pessoa)

print("\n--- Pessoas com 30 anos ou mais ---")
for pessoa in colecao.find({"idade": {"$gte": 30}}):
    print(pessoa)

cliente.close()
