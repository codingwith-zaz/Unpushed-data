from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path('members/', views.members, name='members'),
    path('m/', views.members, name='members1'),
    path('category/', views.category, name='category'),
    path('members/details/<int:id>', views.details, name="Details"),
    path('testing/', views.testing, name="testing"),
]
