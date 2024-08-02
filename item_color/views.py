from django.shortcuts import render
from item_color.forms import AddColorForm
from item_color.models import ItemColor


def add_color(request):
    if request.method == 'POST':
        form = AddColorForm(request.POST)
        if form.is_valid():
            color_name = form.cleaned_data['color_name']
            color_article = form.cleaned_data['color_name']
            color = ItemColor(
                color_name=color_name,
                color_article=color_article
            )
            color.save()
    else:
        form = AddColorForm()
    return render(request, 'item_color/add_color.html', {'form': form})
