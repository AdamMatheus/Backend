from django.urls import path
from .views import (
    # home,
    # todolist,
    # todocreate,
    todoListCreate,
    todo_detail,
    # todo_detail,
    # todo_update,
    # todo_delete,
)


urlpatterns = [
    # path("", home),
    # path("todolist/", todolist),
    # path("todocreate/", todocreate),
    path("todoListCreate/", todoListCreate),
    # path("todo_detail/<int:pk>/", todo_detail),
    # path("todo_update/<int:pk>/", todo_update),
    # path("todo_delete/<int:pk>/", todo_delete),
    path("todo_detail/<int:pk>/", todo_detail),
]