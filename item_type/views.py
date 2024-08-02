from django.shortcuts import render
from item_type.forms import AddTypeForm
from item_type.models import ItemType


# Create your views here.


def add_type(request):
    if request.method == 'POST':
        form = AddTypeForm(request.POST)
        if form.is_valid():
            type_name = form.cleaned_data['type_name']
            type_article = form.cleaned_data['type_article']
            new_type = ItemType(
                type_name=type_name,
                type_article=type_article
            )
            new_type.save()
    else:
        form = AddTypeForm()
    return render(request, 'item_type/add_type.html', {'form': form})
