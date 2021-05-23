from django.urls import path     
from . import views

urlpatterns = [
    path('random_word', views.random_word),
    path('return_page', views.return_page),
    path('new_page', views.new_page),
    # path('counting_page', views.counting_page),
]