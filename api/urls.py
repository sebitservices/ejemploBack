from django.urls import path
from .views import lista_items

urlpatterns = [
    path('items/', lista_items, name='lista_items'),
]
