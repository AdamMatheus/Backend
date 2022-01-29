from django.urls import path
from .views import home, todo_list, todo_add

urlpatterns = [
    path("", home, name="home"),
    path("list/", todo_list, name="list"),
    path("add/", todo_add, name="add"),
]