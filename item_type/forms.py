from django import forms


class AddTypeForm(forms.Form):
    type_name = forms.CharField(max_length=45, label='Наименование')
    type_article = forms.CharField(max_length=3, label='Артикул')
