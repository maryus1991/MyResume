from django.urls import path
from .views import Skill_Selected

urlpatterns = [
    path('<slug:slug>', Skill_Selected, name='Skill_Selected.page')
]