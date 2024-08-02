from django import forms


class AddPrinterForm(forms.Form):
    printer_name = forms.CharField(max_length=40, label='Наименование')
    printer_cost = forms.DecimalField(max_digits=8, decimal_places=2, label='Цена, руб')
    printer_resource = forms.IntegerField(label='Назначенный ресурс, ч')
    print_materials_cost = forms.DecimalField(max_digits=7, decimal_places=2, label='Стоимость расх. мат., руб')
    printer_power = forms.DecimalField(max_digits=3, decimal_places=2, label='Мощность, кВт')
    hour_cost = forms.DecimalField(max_digits=4, decimal_places=2, label='Стоимость 1кВт, руб')
