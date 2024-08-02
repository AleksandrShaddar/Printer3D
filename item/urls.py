from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('add_item/', views.add_item, name='add_item'),
    path('detail/<int:item_id>', views.detail, name='detail'),
    path('settings/', views.settings, name='settings'),
    # path('article/<int:item_id>', views.create_article, name='article'),
]
