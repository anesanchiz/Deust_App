from django.urls import path
from .views import ClienteListView


urlpatterns = [
    path('cliente/', ClienteListView.as_view(), name='cliente_list')
]
