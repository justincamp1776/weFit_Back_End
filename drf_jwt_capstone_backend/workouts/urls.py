from django.urls import path
from .views import WorkoutList
from . import views


urlpatterns = [
    path('', views.WorkoutList.as_view()),
    path('details/<int:id>/', views.WorkoutDetail.as_view()),

]