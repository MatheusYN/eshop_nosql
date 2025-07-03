from faker import Faker
from pymongo import MongoClient
from tqdm import tqdm

fake = Faker('pt_BR')

client = MongoClient("mongodb://mongo:27017/")
db = client["eshop"]
colecao = db["clientes"]

quantidade = 1_000_000

def gerar_cliente():
    return {
        "nome": fake.name(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "cpf": fake.cpf(),
        "endereco": {
            "rua": fake.street_name(),
            "numero": fake.building_number(),
            "cidade": fake.city(),
            "estado": fake.estado_sigla(),
            "cep": fake.postcode()
        },
        "criado_em": fake.date_time_this_decade()
    }

batch_size = 1000
clientes_batch = []

for _ in tqdm(range(quantidade)):
    clientes_batch.append(gerar_cliente())
    if len(clientes_batch) == batch_size:
        colecao.insert_many(clientes_batch)
        clientes_batch = []

if clientes_batch:
    colecao.insert_many(clientes_batch)

print("Inserção finalizada com sucesso.")

