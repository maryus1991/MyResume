from django.urls import path, re_path
from .views import User_index

urlpatterns = [
    path('', User_index, name='index.page'),
]
