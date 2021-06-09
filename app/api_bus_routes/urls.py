from django.urls import path
from . import views

urlpatterns = [
    path('', views.routeList, name="routes"),
    path('detail/<int:pk>/', views.routeDetail, name="details"),
    path('create', views.routeCreate, name="create"),
    path('update/<int:pk>/', views.routeUpdate, name="update"),
    path('delete/<int:pk>/', views.routeDelete, name="delete"),
    path('search', views.routeSearch, name="search"),
    path('findroute/<str:start>/<str:end>/', views.findNeedRoute, name="find")
]
