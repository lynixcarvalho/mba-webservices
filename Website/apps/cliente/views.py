from django.shortcuts import render
import requests

from .forms import IdForm, SearchForm, RegisterForm, UpdateForm

urlAPI = 'http://cliente_api:8000'


# Create your views here.
def cliente_lista(request):

    # pull data from third party rest api
    response = requests.get(f"{urlAPI}/cliente")

    # convert reponse data into json
    clientes = response.json()

    for cliente in clientes:
        cliente['id'] = cliente.pop('_id')

    return render(request, "cliente_lista.html", {'clientes': clientes})


def cliente_search(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            response = None

            if form.cleaned_data['id']:
                cliente_consulta = form.cleaned_data['id']
                # pull data from third party rest api
                response = requests.get(f"{urlAPI}/cliente/{cliente_consulta}")
                # convert reponse data into json
                clientes = list(response.json())

                for cliente in clientes:
                    cliente['id'] = cliente.pop('_id')

                return render(request, "cliente_single.html", {'clientes': clientes})

            elif form.cleaned_data['name']:
                cliente_consulta = form.cleaned_data['name']
                # pull data from third party rest api
                response = requests.get(f"{urlAPI}/cliente?name={cliente_consulta}")
                # convert reponse data into json
                clientes = list(response.json())

                for cliente in clientes:
                    cliente['id'] = cliente.pop('_id')

                return render(request, "cliente_single.html", {'clientes': clientes})

            else:
                return render(request, 'cliente_search.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm

    return render(request, 'cliente_search.html', {'form': form})


def cliente_search_id(request, cliente_id):

    response = requests.get(f"{urlAPI}/cliente/{cliente_id}")
    clientes = list(response.json())

    for cliente in clientes:
        cliente['id'] = cliente.pop('_id')

    return render(request, "cliente_single.html", {'clientes': clientes})


def cliente_create(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            cliente_name = form.cleaned_data['name']
            cliente_address = form.cleaned_data['address']
            gen_card = form.cleaned_data['gen_card']

            cliente = {
                "name": cliente_name,
                "address": cliente_address,
                "gen_card": gen_card
            }

            # pull data from third party rest api
            response = requests.post(f"{urlAPI}/cliente", json=cliente)

            # convert response data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'cliente_create.html', {'form': form})


def cliente_delete(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = IdForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            cliente_id = form.cleaned_data['id']

            # pull data from third party rest api
            response = requests.delete(f"{urlAPI}/cliente/{cliente_id}")

            # convert reponse data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IdForm()

    return render(request, 'cliente_delete.html', {'form': form})


def cliente_update(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = UpdateForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            cliente_id = form.cleaned_data['id']
            cliente_name = form.cleaned_data['name']
            cliente_address = form.cleaned_data['address']

            cliente = {
                "name": cliente_name,
                "address": cliente_address
            }

            # pull data from third party rest api
            response = requests.put(f"{urlAPI}/cliente/{cliente_id}", json=cliente)

            # convert reponse data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateForm()

    return render(request, 'cliente_update.html', {'form': form})
