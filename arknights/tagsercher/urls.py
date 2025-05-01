from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tagsercher_view, name='tagsercher'),
    path('addoperator', views.add_operator_form_view, name='addoperator'),
]