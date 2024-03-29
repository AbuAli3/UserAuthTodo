from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoList, name='home'),  # Map the home page URL to the todoList view
    path('register/', views.userRegister, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('todo/', views.todoList, name='todoList'),
    path('todo/add/', views.addTodo, name='addTodo'),
    path('todo/del/<int:item_id>/', views.delTodo, name='delTodo'),

]
