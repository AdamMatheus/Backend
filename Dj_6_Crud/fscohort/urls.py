from django.urls import path
from .views import home_page, student_list, student_add

urlpatterns = [
    path('', home_page, name="home"),
    path('student_list/', student_list, name="list"),
    path('student_add/', student_add, name="add"),

]