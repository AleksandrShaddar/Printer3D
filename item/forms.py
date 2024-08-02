from django import forms

from item.models import Item
from item_model.models import ItemModel
from item_type.models import ItemType
from plastic.models import Plastic
from printer.models import Printer


class AddItemForm(forms.Form):
    item_type = forms.ModelChoiceField(ItemType.objects.all(), label='Тип изделия')
    item_name = forms.ModelChoiceField(ItemModel.objects.all(), label='Наименование')
    item_size = forms.IntegerField(label='Типоразмер')
    item_mass = forms.DecimalField(max_digits=7, decimal_places=2, label='Масса отпечатка, гр')
    print_time = forms.IntegerField(label='Время отпечатка, мин')


class SettingsForm(forms.Form):
    printer = forms.ModelChoiceField(Printer.objects.all(), label='Выберите принтер')
    plastic = forms.ModelChoiceField(Plastic.objects.all(), label='Выберите пластик')
