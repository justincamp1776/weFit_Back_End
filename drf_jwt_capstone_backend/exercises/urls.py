from django.urls import path
from .views import ExerciseList
from . import views


urlpatterns = [
    path('', views.ExerciseList.as_view())
]
