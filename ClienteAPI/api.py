import re
import requests
from typing import Optional
from fastapi import FastAPI
from models import Item, UpdateItem, UpdateCardItem
from random import randint
from mongo_con import collection


app = FastAPI()
urlAPI = "http://cartao_api:9200"


def generate_id():
    s = ''
    for i in range(6):
        s += str(randint(0, 9))
    return s


@app.get('/cliente')
def cliente_search(
        name: Optional[str] = None,
        address: Optional[str] = None):

    try:
        if name:
            cliente = list(filter(lambda x: re.search(name, x['name']), collection.find()))
        elif address:
            cliente = list(filter(lambda x: re.search(address, x['address']), collection.find()))
        else:
            cliente = list(map(lambda x: x, collection.find({})))
        return cliente

    except Exception as err:
        return {'msg': err}


@app.get('/cliente/{item_id}')
def cliente_search_id(item_id):

    cliente = list(filter(lambda x: x["_id"] == item_id, collection.find({})))

    if not cliente:
        return {'msg': 'Cliente não cadastrado na base'}

    return cliente


@app.post('/cliente')
def cliente_create(item: Item):

    item = item.dict()
    gen_id = True

    # Loop que chama a função generate_id(), que gera ID aleatório de 6 dígitos, e atribui à variável item.
    # Se o ID já estiver em uso, executa novamente a função generate_id().
    # Se o ID gerado não estiver em uso, variável gen_id é setada para False e finaliza o loop while.
    while gen_id is True:
        # Chamada a função generate_id()
        item['_id'] = generate_id()
        # Consulta a base para checar se o ID já está em uso.
        search = list(filter(lambda x: x, collection.find({'_id': item['_id']})))

        # Checagem se o ID está em uso
        if not search:
            gen_id = False

    # Se no cadastro do cliente o checkbox de gerar cartão estiver marcado (True), é gerado um número de cartão
    # e adicionado ao cadastro do cliente
    if item['gen_card']:
        cliente = {
            "cliente_id": item["_id"],
            "limite": 1000
        }

        response = requests.post(f"{urlAPI}/cartao_from_cliente", json=cliente)
        card = response.json()['card']
        item['card'] = []
        item['card'].append(card)

    try:
        search = list(filter(lambda x: x, collection.find(item, {'_id': 0})))
        if search:
            return {'msg': 'Cliente já cadastrado na base.'}

        collection.insert_one(item)
        return {'msg': 'Cliente adicionado com sucesso.'}
    except Exception as err:
        return {'msg': err}


@app.delete('/cliente/{item_id}')
def cliente_delete(item_id):

    try:

        search = list(filter(lambda x: x["_id"] == item_id, collection.find({})))

        if not search:
            return {'msg': 'Cliente não cadastrado na base.'}

        cartoes = search[0]['card']

        for cartao in cartoes:
            response = requests.delete(f"{urlAPI}/cartao/{cartao}")

        collection.delete_one(search[0])
        return {'msg': 'Cliente removido com sucesso.'}

    except Exception as err:
        return {'msg': err}


@app.put('/cliente/{item_id}')
def cliente_update(item_id, item: UpdateItem):

    try:

        cliente = collection.find_one({'_id': item_id})

        if not cliente:
            return {'msg': 'Cliente não cadastrado na base.'}

        if item.name is not None and item.address is not None:
            cliente['name'] = item.name
            cliente['address'] = item.address
            collection.find_one_and_replace({'_id': item_id}, cliente)
            return {'msg': 'Cliente atualizado com sucesso.'}
        else:
            return {'msg': 'Atualização de cliente exige o preenchimento dos campos nome e endereco'}

    except Exception as err:
        return {'msg': err}


@app.patch('/cliente_from_card/{item_id}')
def update_cliente_from_card(item_id, item: UpdateCardItem):

    try:
        cliente = collection.find_one({'_id': item_id})

        if not cliente:
            return {'msg': 'Cliente não cadastrado na base'}

        if cliente['card']:
            cliente['card'].append(item.card)
        else:
            cliente['card'] = item.card

        collection.find_one_and_replace({'_id': item_id}, cliente)

        return {'msg': 'Cliente atualizado com sucesso.'}

    except Exception as err:
        return {'msg': err}


@app.patch('/cliente/{item_id}')
def update_cliente_partial(item_id, item: UpdateItem):

    try:
        cliente = collection.find_one({'_id': item_id})

        if not cliente:
            return {'msg': 'Cliente não cadastrado na base'}

        if cliente['card']:
            cliente['card'].append(item.card[0])

        else:
            cliente['card'] = item.card[0]

        collection.find_one_and_replace({'_id': item_id}, cliente)

        return {'msg': 'Cliente atualizado com sucesso.'}

    except Exception as err:
        return {'msg': err}
