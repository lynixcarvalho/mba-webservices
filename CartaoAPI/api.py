import re
from typing import Optional
from fastapi import FastAPI
from models import Item, UpdateItem
from uuid import uuid4
from random import randint
from mongo_con import collection, collection2
import requests
# import datetime

app = FastAPI()
urlAPI = "http://cliente_api:9100"
# data = datetime.datetime.now() + datetime.timedelta(days=3*365)


def generate_card():
    s = '99'
    for i in range(14):
        s += str(randint(0, 9))
    return s


@app.get('/cartao')
def cartao_search():

    try:

        cartao = list(map(lambda x: x, collection.find({})))

        return cartao

    except Exception as err:
        return {'Msg': err}


@app.get('/cartao/{item_id}')
def cartao_search_id(item_id):

    cartao = list(filter(lambda x: x["_id"] == item_id, collection.find({})))

    if not cartao:
        return {'Error': 'Cartão não cadastrado na base.'}

    return cartao


@app.post('/cartao_from_cliente')
def cartao_create_from_cliente(item: Item):

    item = item.dict()
    gen_card = True

    try:
        while gen_card is True:
            # Chamada a função generate_id()
            item['_id'] = generate_card()
            # Consulta a base para checar se o ID já está em uso.
            search = list(filter(lambda x: x, collection.find({'_id': item['_id']})))

            # Checagem se o ID está em uso
            if not search:
                gen_card = False

        collection.insert_one(item)

        return {'msg': 'Cartão adicionado com sucesso!', 'card': item['_id']}

    except Exception as err:
        return {'msg': err}


@app.post('/cartao')
def cartao_create_new(item: Item):

    item = item.dict()
    # item['vencimento'] = data.strftime("%Y-%m-%d")
    gen_card = True

    try:
        while gen_card is True:
            # Chamada a função generate_id()
            item['_id'] = generate_card()
            # Consulta a base para checar se o ID já está em uso.
            search = list(filter(lambda x: x, collection.find({'_id': item['_id']})))

            # Checagem se o ID está em uso
            if not search:
                gen_id = False

        cliente = list(filter(lambda x: x, collection2.find({'_id': item['cliente_id']})))

        cartao = {
            "card": item['_id']
        }

        response = requests.patch(f"{urlAPI}/cliente_from_card/{cliente[0]['_id']}", json=cartao)

        if response.json()['msg'] == 'Cliente atualizado com sucesso.':

            collection.insert_one(item)

            return {'msg': 'Cartao adicionado com sucesso!'}

        else:
            return response.json()

    except Exception as err:
        return {'msg': err}


@app.delete('/cartao/{item_id}')
def cartao_delete(item_id):

    try:

        cartao = list(filter(lambda x: x["_id"] == item_id, collection.find({})))

        if not cartao:
            return {'msg': 'Cartão não cadastrado na base.'}

        collection.delete_one(cartao[0])
        return {'msg': 'Cartão removido com sucesso.'}

    except Exception as err:
        return {'msg': err}


# @app.put('/cartao/{id}')
# def update_client(id, item: UpdateItem):
#
#     try:
#
#         card = collection.find_one({'_id': id})
#
#         if not card:
#             return {'Error': 'Card does not exist'}
#
#         if item.card_limit is not None:
#             card['card_limit'] = item.card_limit
#             collection.find_one_and_replace({'_id': id}, card)
#             return {'Msg': 'Card atualizado com sucesso.'}
#         else:
#             return {'Error': 'Operação de update exige os campos name e address'}
#
#     except Exception as err:
#         return {'Error': err}
