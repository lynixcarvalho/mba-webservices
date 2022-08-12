from django import forms


class SearchForm(forms.Form):
    number = forms.CharField(label='Número do cartão', max_length=100)


class RegisterForm(forms.Form):
    cliente_id = forms.CharField(label='ID do Cliente', max_length=100)
    limite = forms.FloatField(label='Limite do cartão', required=False)


class UpdateForm(forms.Form):
    number = forms.CharField(label='Número do cartão', max_length=100)
    limite = forms.FloatField(label='Limite do cartão', required=False)
