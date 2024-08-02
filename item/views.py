from django.db.models import OuterRef, Subquery
from django.shortcuts import render
from item.forms import AddItemForm, SettingsForm
from item.models import Item, Settings
from item_color.models import ItemColor
from item_model.models import ItemModel
from item_type.models import ItemType
from plastic.models import Plastic
from printer.models import Printer

# Create your views here.


def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item_type = form.cleaned_data['item_type']
            item_name = form.cleaned_data['item_name']
            item_size = form.cleaned_data['item_size']
            item_mass = form.cleaned_data['item_mass']
            print_time = form.cleaned_data['print_time']
            item = Item(
                type_item=item_type,
                item_name=item_name,
                size_type=item_size,
                print_mass=item_mass,
                print_time=print_time)
            item.save()
    else:
        form = AddItemForm()
    return render(request, 'item/add_item.html', {'form': form})


def main_view(request):
    items = Item.objects.all()
    unique_items = {}
    for item in items:
        unique_items[item.item_name] = item
    unique_items_list = list(unique_items.values())
    quantity = len(unique_items_list)
    context = {'unique_items_list': unique_items_list, 'quantity': quantity}
    return render(request, 'item/main.html', context)


def detail(request, item_id):
    if Settings.objects.first() is None:
        return settings(request)
    printer = Printer.objects.get(id=Settings.objects.first().printer_id)
    plastic = Plastic.objects.get(id=Settings.objects.first().plastic_id)
    item = Item.objects.get(id=item_id)
    aaa = ItemType.objects.get(id=item.type_item_id).type_article
    bbb = ItemModel.objects.get(id=item.item_name_id).model_article
    ccc = ItemColor.objects.get(id=Plastic.objects.get(id=Settings.objects.first().plastic_id).plastic_color_id).color_article
    sizes = Item.objects.filter(item_name_id=item.item_name_id).values_list('size_type', flat=True).distinct()
    if request.method == 'POST':
        ddd = request.POST.get('size')
        print_time = Item.objects.filter(item_name_id=item.item_name_id, size_type=ddd).first().print_time
        print_mass = Item.objects.filter(item_name_id=item.item_name_id, size_type=ddd).first().print_mass
        article = f'{aaa}-{bbb}-{ccc}-{ddd}'
        printer_cost = (printer.printer_cost + printer.print_materials_cost)/printer.printer_resource
        printering_time = print_time/60
        cost = float(printer_cost) * printering_time + float(printer.hour_cost)*printering_time + float(print_mass * plastic.plastic_price)
        final_cost = round(cost * 3, 2)
        context = {'item': item, 'article': article, 'print_time': print_time,
                   'print_mass': print_mass, 'sizes': sizes, 'ddd': ddd, 'cost': round(cost, 2), 'final_cost': final_cost}
        return render(request, 'item/detail.html', context)
    else:
        return render(request, 'item/detail.html', {'item': item, 'sizes': sizes})


def settings(request):
    message = 'Предыдущих настроек не найдено!'
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            printer = form.cleaned_data['printer']
            plastic = form.cleaned_data['plastic']
            if Settings.objects.first() is not None:
                tem_set = Settings.objects.update(
                    printer=printer,
                    plastic=plastic
                )
            else:
                tem_set = Settings(
                    printer=printer,
                    plastic=plastic
                )
                tem_set.save()
            message = 'Настройки сохранены!'
    else:
        if Settings.objects.first() is not None:
            message = (f'Последние настройки: '
                       f'Принтер: {Settings.objects.first().printer} '
                       f'Пластик: {Settings.objects.first().plastic}')
        form = SettingsForm()
    return render(request, 'item/settings.html', {'form': form, 'message': message})
