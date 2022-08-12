from django import forms


class IdForm(forms.Form):
    id = forms.CharField(label='ID do Cliente', max_length=100)


class SearchForm(forms.Form):
    id = forms.CharField(label='ID do Cliente', max_length=100, required=False)
    name = forms.CharField(label='Nome do Cliente', max_length=100, required=False)


class RegisterForm(forms.Form):
    name = forms.CharField(label='Nome Completo', max_length=100)
    address = forms.CharField(label='Endereço', max_length=100)
    gen_card = forms.BooleanField(label='Gerar cartão?', required=False)


class UpdateForm(forms.Form):
    id = forms.CharField(label='ID do Cliente', max_length=100)
    name = forms.CharField(label='Nome do Cliente', max_length=100)
    address = forms.CharField(label='Endereço ', max_length=100)
