from django import forms
from item_type.models import ItemType


class AddModelForm(forms.Form):
    model_name = forms.CharField(max_length=45, label='Наименование')
    model_article = forms.CharField(max_length=3, label='Артикул')
    model_type = forms.ModelChoiceField(ItemType.objects.all(), label='Тип модели')
