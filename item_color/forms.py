from django import forms


class AddColorForm(forms.Form):
    color_name = forms.CharField(max_length=45, label='Наименование')
    color_article = forms.CharField(max_length=3, label='Артикул')
