from django.shortcuts import render
from printer.forms import AddPrinterForm
from printer.models import Printer


# Create your views here.

def add_printer(request):
    message = 'Для добавления принтера заполните следующие поля:'
    if request.method == 'POST':
        form = AddPrinterForm(request.POST)
        if form.is_valid():
            printer_name = form.cleaned_data['printer_name']
            printer_cost = form.cleaned_data['printer_cost']
            printer_resource = form.cleaned_data['printer_resource']
            print_materials_cost = form.cleaned_data['print_materials_cost']
            printer_power = form.cleaned_data['printer_power']
            hour_cost = form.cleaned_data['hour_cost']
            printer = Printer(
                printer_name=printer_name,
                printer_cost=printer_cost,
                printer_resource=printer_resource,
                print_materials_cost=print_materials_cost,
                printer_power=printer_power,
                hour_cost=hour_cost
            )
            printer.save()
            message = 'Принтер успешно добавлен!'
            form = AddPrinterForm()
    else:
        form = AddPrinterForm()
    return render(request, 'printer/add_printer.html',
                  {'form': form, 'message': message})

