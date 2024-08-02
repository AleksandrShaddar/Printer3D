from django.db import models

# Create your models here.


class ItemType(models.Model):
    type_name = models.CharField(max_length=45)
    type_article = models.CharField(max_length=3)

    def __str__(self):
        return self.type_name
