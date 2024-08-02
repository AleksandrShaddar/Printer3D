from django.shortcuts import render
from item_model.forms import AddModelForm
from item_model.models import ItemModel


# Create your views here.


def add_model(request):
    if request.method == 'POST':
        form = AddModelForm(request.POST)
        if form.is_valid():
            model_name = form.cleaned_data['model_name']
            model_article = form.cleaned_data['model_article']
            model_type = form.cleaned_data['model_type']
            model = ItemModel(
                model_name=model_name,
                model_article=model_article,
                model_type=model_type
            )
            model.save()
    else:
        form = AddModelForm()
    return render(request, 'item_model/add_model.html', {'form': form})
