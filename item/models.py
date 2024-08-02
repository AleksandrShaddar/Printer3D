from django.db import models
from item_model.models import ItemModel
from item_type.models import ItemType
from plastic.models import Plastic
from printer.models import Printer


# Create your models here.


class Item(models.Model):
    type_item = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    item_name = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    size_type = models.CharField(max_length=4)
    print_mass = models.DecimalField(max_digits=5, decimal_places=2)
    print_time = models.PositiveIntegerField()


class Settings(models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    plastic = models.ForeignKey(Plastic, on_delete=models.CASCADE)
