from django.urls import path
from .views import index, login_view, update_todo_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('update_todo/', update_todo_view, name='update_todo'),
]
