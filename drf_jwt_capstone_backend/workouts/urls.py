from django.urls import path
from .views import WorkoutList
from .views import WorkoutDetail
from . import views


urlpatterns = [
    path('', views.WorkoutList.as_view()),
    path('details/<int:pk>/', views.WorkoutDetail.as_view()),
]