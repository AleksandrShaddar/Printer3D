from django.db import models

# Create your models here.


class ItemColor(models.Model):
    color_name = models.CharField(max_length=45, unique=True)
    color_article = models.CharField(max_length=3)

    def __str__(self):
        return self.color_name
