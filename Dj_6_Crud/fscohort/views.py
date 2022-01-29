from django.shortcuts import render
from django.http import HttpResponse

# def home_page(request):
#     return HttpResponse("we are developers")

def home_page(request):
    return render(request, "fscohort/home.html")
