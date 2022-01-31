
from django.shortcuts import redirect, render

from student.models import Student
from .forms import StudentForm

def index(request):
     return render(request, 'student/index.html')

# def student_page(request):
#     print(request.POST)
#     print(request.FILES)
#     form = StudentForm()
#     context = {
#         'form': form
#     }
#     return render(request,'student/student.html', context)
# # Create your views here.

# def student_page(request):
#     form = StudentForm()
#     if request.method == 'POST':
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             student_data = {
#                 "first_name": form.cleaned_data.get('first_name'),
#                 "last_name": form.cleaned_data.get('last_name'),
#                 "number": form.cleaned_data.get('number'),
#                 "profile_pic": form.cleaned_data.get('profile_image'),
#             }
#             student = Student(**student_data)
#             student.save()
#             return redirect('home')

#     context = {
#         'form': form
#     }
#     return render(request, 'student/student.html', context)


def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')

    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)