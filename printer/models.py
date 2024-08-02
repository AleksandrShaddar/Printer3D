from django.db import models

# Create your models here.


class Printer(models.Model):
    printer_name = models.CharField(max_length=40)
    printer_cost = models.DecimalField(max_digits=8, decimal_places=2)
    printer_resource = models.IntegerField()
    print_materials_cost = models.DecimalField(max_digits=7, decimal_places=2)
    printer_power = models.DecimalField(max_digits=3, decimal_places=2)
    hour_cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.printer_name
