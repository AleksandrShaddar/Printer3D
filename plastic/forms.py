from django import forms
from item_color.models import ItemColor


class AddPlasticForm(forms.Form):
    name = forms.CharField(max_length=45, label='Наименование')
    plastic_type = forms.CharField(max_length=45, label='Тип пластика')
    plastic_color = forms.ModelChoiceField(ItemColor.objects.all(), label='Цвет пластика')
    plastic_price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена, руб/гр')
