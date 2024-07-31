from django.urls import path
from .views import index, login_view, update_todo_view
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('update_todo/', update_todo_view, name='update_todo'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
