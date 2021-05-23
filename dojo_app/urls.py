from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('some_function', views.some_function),
    path('result', views.result),
]