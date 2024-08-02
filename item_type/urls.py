from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_type, name='add_type')
]
