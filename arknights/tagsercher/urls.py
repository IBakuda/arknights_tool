from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tagsercher_view, name='tagsercher'),
    path('addoperator', views.add_operator_form_view, name='addoperator'),
    path('editoperator', views.operator_edit_view, name='editoperator'),
]