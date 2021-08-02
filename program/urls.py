from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create', create, name='create_program'),
    path('search', SearchListView.as_view(), name='search_res')
]
