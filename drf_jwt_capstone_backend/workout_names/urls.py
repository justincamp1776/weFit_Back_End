from django.urls import path
from .views import WorkoutNameList
from . import views


urlpatterns = [
    path('', views.WorkoutNameList.as_view()),
]