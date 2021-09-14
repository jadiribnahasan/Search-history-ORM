from django.urls import path
from .views import index, filter

app_name = 'main'

urlpatterns = [
    path('', index, name="home"),
    path('getFilteredItems/', filter, name='getFilteredItems'),
]
