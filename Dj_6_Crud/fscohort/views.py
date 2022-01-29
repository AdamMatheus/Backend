from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# def home_page(request):
#     return HttpResponse("we are developers")

def home_page(request):
    return render(request, "fscohort/home.html")

def student_list (request):
    students=Student.objects.all()
    context={
        "students":students
    }
    
    return render(request,'fscohort/student_list.html',context)
    
def student_add(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context={
        "form":form
    } 
    
    return render(request,"fscohort/student_add.html",context)