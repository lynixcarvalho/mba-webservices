from django.shortcuts import render
import requests

from .forms import SearchForm, RegisterForm, UpdateForm

urlAPI = "http://cartao_api:9200"


# Create your views here.
def cartao_lista(request):

    # pull data from third party rest api
    response = requests.get(f"{urlAPI}/cartao")

    # convert reponse data into json
    cartao = response.json()

    for card in cartao:
        card['id'] = card.pop('_id')

    return render(request, "cartao_lista.html", {'cartao': cartao})


def cartao_search(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            response = None

            if form.cleaned_data['number']:
                cartao_consulta = form.cleaned_data['number']
                # pull data from third party rest api
                response = requests.get(f"{urlAPI}/cartao/{cartao_consulta}")
                # convert reponse data into json
                cartoes = list(response.json())

                for cartao in cartoes:
                    cartao['id'] = cartao.pop('_id')

                return render(request, "cartao_single.html", {'cartoes': cartoes})

            else:
                return render(request, 'cartao_search.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm

    return render(request, 'cartao_search.html', {'form': form})


def cartao_search_number(request, number):

    response = requests.get(f"{urlAPI}/cartao/{number}")

    cartoes = list(response.json())

    for cartao in cartoes:
        cartao['id'] = cartao.pop('_id')

    return render(request, "cartao_single.html", {'cartoes': cartoes})


def cartao_create(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            cliente_id = form.cleaned_data['cliente_id']
            limite = form.cleaned_data['limite']

            cartao = {
                "cliente_id": cliente_id,
                "limite": limite,
            }

            # pull data from third party rest api
            response = requests.post(f"{urlAPI}/cartao", json=cartao)

            # convert response data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'cartao_create.html', {'form': form})


def cartao_delete(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            number = form.cleaned_data['number']

            # pull data from third party rest api
            response = requests.delete(f"{urlAPI}/cartao/{number}")

            # convert reponse data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'cartao_delete.html', {'form': form})
