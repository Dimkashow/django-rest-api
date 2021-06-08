from django.urls import path
from . import views

urlpatterns = [
    path('', views.routeList, name="routes"),
    path('detail/<int:pk>/', views.routeDetail, name="details"),
    path('create', views.routeCreate, name="create"),
    path('update/<int:pk>/', views.routeUpdate, name="update"),
    path('delete/<str:pk>/', views.routeDelete, name="delete"),
]
