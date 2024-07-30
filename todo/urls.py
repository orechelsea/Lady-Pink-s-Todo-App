from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('update/', views.update_todo, name='update_todo'),
]
