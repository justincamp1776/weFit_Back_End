from django.urls import path
from .views import NameList
from .views import NameDetail
from . import views


urlpatterns = [
    path('', views.NameList.as_view()),
    path('<int:pk>/', views.NameDetail.as_view())
]