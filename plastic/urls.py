from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_plastic, name='add_plastic'),
]
