from django.urls import path, re_path
from .views import User_index

urlpatterns = [
    path('<slug:slug>', User_index, name='Skill_Selected.page'),
    path('', User_index, name='index.page'),
]
