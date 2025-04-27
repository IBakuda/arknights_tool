from django.urls import path
from . import views
from .views import StoryCostAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('m', views.create_model_data, name='m'),
    path('f', views.edit_stories, name='f'),
    path('playeredit', views.edit_player, name='playeredit'),
    path('api/v1/srorycost/', StoryCostAPIView.as_view())
]