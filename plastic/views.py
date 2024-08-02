from django.shortcuts import render
from plastic.forms import AddPlasticForm
from plastic.models import Plastic


# Create your views here.

def add_plastic(request):
    if request.method == 'POST':
        form = AddPlasticForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            plastic_type = form.cleaned_data['plastic_type']
            plastic_color = form.cleaned_data['plastic_color']
            plastic_price = form.cleaned_data['plastic_price']
            plastic = Plastic(
                name=name,
                plastic_type=plastic_type,
                plastic_color=plastic_color,
                plastic_price=plastic_price
            )
            plastic.save()
    else:
        form = AddPlasticForm()
    return render(request, 'plastic/add_plastic.html', {'form': form})
