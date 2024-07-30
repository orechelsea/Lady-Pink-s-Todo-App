from django.urls import path
from .views import update_todo


urlpatterns = [
    path('', views.index, name='home'),
    path('update/', update_todo.as_view(), name='update_todo'),
]
