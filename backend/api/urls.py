from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, RegisterView, LoginView

urlpatterns = [

    path('todos/', TodoListCreateView.as_view(), name = 'todos_list_create'),
    path('todos/<int:pk>', TodoRetrieveUpdateDestroyView.as_view(), name = 'todos_retrieve_update_destroy'),

    #User registration and login
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login'),
]