from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_color, name='add_color'),
]
