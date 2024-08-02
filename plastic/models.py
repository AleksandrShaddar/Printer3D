from django.db import models
from item_color.models import ItemColor

# Create your models here.


class Plastic(models.Model):
    name = models.CharField(max_length=45)
    plastic_type = models.CharField(max_length=45)
    plastic_color = models.ForeignKey(ItemColor, on_delete=models.CASCADE)
    plastic_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.plastic_type} ({self.plastic_color})'
