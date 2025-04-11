from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('m', views.create_model_data, name='m')
]