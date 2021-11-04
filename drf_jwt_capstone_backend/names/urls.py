from django.urls import path
from .views import NameList
from . import views


urlpatterns = [
    path('', views.NameList.as_view()),
]