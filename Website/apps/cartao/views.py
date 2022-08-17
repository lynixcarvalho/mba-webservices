from django.shortcuts import render
import requests

from .forms import SearchForm, RegisterForm, UpdateForm

urlAPI = "http://cartao_api:9200/cartoes"


# Create your views here.
def lista(request):

    # pull data from third party rest api
    response = requests.get(f"{urlAPI}")

    # convert reponse data into json
    cartoes = response.json()

    for cartao in cartoes:
        cartao['id'] = cartao.pop('_id')

    return render(request, "cartoes/lista.html", {'cartoes': cartoes})


def search(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            if form.cleaned_data['number']:
                number = form.cleaned_data['number']

                response = requests.get(f"{urlAPI}/{number}")

                if response.json() == {'msg': 'Cartão não cadastrado na base.'}:
                    return render(request, "index.html", response.json())

                cartoes = list(response.json())

                for cartao in cartoes:
                    cartao['id'] = cartao.pop('_id')

                return render(request, "cartoes/search_one.html", {'cartoes': cartoes})

            else:
                return render(request, 'cartoes/search.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm

    return render(request, 'cartoes/search.html', {'form': form})


def search_number(request, number):

    response = requests.get(f"{urlAPI}/{number}")

    if response.json() == {'msg': 'Cartão não cadastrado na base.'}:
        return render(request, "index.html", response.json())

    cartoes = list(response.json())

    for cartao in cartoes:
        cartao['id'] = cartao.pop('_id')

    return render(request, "cartoes/search_one.html", {'cartoes': cartoes})


def create(request):

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
            response = requests.post(f"{urlAPI}", json=cartao)

            # convert response data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'cartoes/create.html', {'form': form, 'resource': 'cartoes'})


def delete(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            number = form.cleaned_data['number']

            # pull data from third party rest api
            response = requests.delete(f"{urlAPI}/{number}")

            # convert reponse data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'cartoes/delete.html', {'form': form, 'resource': 'cartoes'})


def update(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = UpdateForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            number = form.cleaned_data['number']
            limite = form.cleaned_data['limite']

            cartao = {
                "limite": limite
            }

            # pull data from third party rest api
            response = requests.patch(f"{urlAPI}/{number}", json=cartao)

            # convert reponse data into json
            msg = response.json()

            return render(request, "index.html", {'msg': msg['msg']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateForm()

    return render(request, 'cartoes/update.html', {'form': form, 'resource': 'cartoes'})
