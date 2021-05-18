from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateRepport.as_view(), name="report"),
]
