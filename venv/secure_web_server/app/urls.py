from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('secure/', views.secure_view, name='secure_view'),
]