from django.urls import path
from .views import GoalDetail
from .views import GoalList
from .views import GoalCollection
from . import views


 

urlpatterns = [
    path('', views.GoalList.as_view()),
    path('details/<int:pk>/', views.GoalDetail.as_view()),
    path('<int:user_id>/', views.GoalCollection.as_view())
    ]   