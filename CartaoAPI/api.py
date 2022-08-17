from fastapi import FastAPI
from models import Item, UpdateItem
from random import randint
from mongo_con import collection, collection2
import requests
import datetime

app = FastAPI()
urlAPI = "http://cliente_api:9100"


def generate_card():
    card_number = '99'
    cvv = ''

    for i in range(14):
        card_number += str(randint(0, 9))

    for i in range(3):
        cvv += str(randint(0, 9))

    data_vcto = datetime.datetime.now() + datetime.timedelta(days=3*365)

    card = {
        "number": card_number,
        "cvv": cvv,
        "limite": 1000,
        "data_vcto": data_vcto.isoformat()[0:10]
    }

    return card


@app.get('/cartoes')
def cartao_search():

    try:

        cartao = list(map(lambda x: x, collection.find({})))

        return cartao

    except Exception as err:
        return {'msg': err}


@app.get('/cartoes/{item_id}')
def cartao_search_id(item_id):

    cartao = list(filter(lambda x: x["_id"] == item_id, collection.find({})))

    if not cartao:
        return {'msg': 'Cartão não cadastrado na base.'}

    return cartao


@app.post('/cartao_from_cliente')
def cartao_create_from_cliente(item: Item):

    item = item.dict()
    gen_card = True

    try:
        while gen_card is True:
            # Chamada a função generate_card()
            item = generate_card()
            item['_id'] = item.pop('number')

            # Consulta a base para checar se o ID já está em uso.
            search = list(filter(lambda x: x, collection.find({'_id': item['_id']})))

            # Checagem se o ID está em uso
            if not search:
                gen_card = False

        collection.insert_one(item)

        return {'msg': 'Cartão adicionado com sucesso!', 'card': item['_id']}

    except Exception as err:
        return {'msg': err}


@app.post('/cartoes')
def cartao_create_new(item: Item):

    item = item.dict()
    gen_card = True

    try:
        while gen_card is True:
            # Chamada a função generate_card()
            item = generate_card()
            item['_id'] = item.pop('number')

            # Consulta a base para checar se o ID já está em uso.
            search = list(filter(lambda x: x, collection.find({'_id': item['_id']})))

            # Checagem se o ID está em uso
            if not search:
                gen_card = False

        cliente = list(filter(lambda x: x, collection2.find({'_id': item['cliente_id']})))

        if cliente:

            cartao = {
                "card": item['_id']
            }

            response = requests.patch(f"{urlAPI}/cliente_from_card/{cliente[0]['_id']}", json=cartao)

            if response.json()['msg'] == 'Cliente atualizado com sucesso.':

                collection.insert_one(item)

                return {'msg': 'Cartao adicionado com sucesso!'}

            else:
                return response.json()

        else:
            return {'msg': 'Cliente informado não cadastrado na base.'}

    except Exception as err:
        return {'msg': err}


@app.delete('/cartoes/{item_id}')
def cartao_delete(item_id):

    try:

        cartao = list(filter(lambda x: x["_id"] == item_id, collection.find({})))

        if not cartao:
            return {'msg': 'Cartão não cadastrado na base.'}

        cliente_id = cartao[0]['cliente_id']
        print(cliente_id)
        cliente = list(filter(lambda x: x, collection2.find({'_id': cliente_id})))
        print(cliente)
        cartoes = cliente[0]['card']
        print(cartoes)
        # cartoes.pop(item_id)
        cartoes.pop(cartoes.index(item_id))

        collection2.find_one_and_replace({'_id': cliente_id}, cliente[0])

        collection.delete_one(cartao[0])
        return {'msg': 'Cartão removido com sucesso.'}

    except Exception as err:
        return {'msg': err}


@app.patch('/cartoes/{item_id}')
def update_cartao(item_id, item: UpdateItem):

    try:

        card = collection.find_one({"_id": item_id})

        if not card:
            return {"msg": "Cartão não cadastrado na base."}

        collection.update_one({"_id": item_id}, {"$set": {"limite": item.limite}})

        return {"msg": "Limite do cartão alterado com sucesso."}

    except Exception as err:
        return {'msg': err}
