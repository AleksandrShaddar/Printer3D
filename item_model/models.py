from django.db import models
from item_type.models import ItemType


# Create your models here.


class ItemModel(models.Model):
    model_name = models.CharField(max_length=45)
    model_article = models.CharField(max_length=3)
    model_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name
