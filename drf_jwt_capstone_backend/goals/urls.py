from django.urls import path
from .views import GoalDetail
from .views import GoalList
from . import views


 

urlpatterns = [
    path('', views.GoalList.as_view()),
    path('details/<int:user_id>/', views.GoalDetail.as_view())
    ]   