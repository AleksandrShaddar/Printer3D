from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_printer, name='add_printer')
]
