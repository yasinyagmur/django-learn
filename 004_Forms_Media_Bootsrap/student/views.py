from multiprocessing import context
from django.shortcuts import render



# Create your views here.
from django.shortcuts import render
from .forms import StudentForm


def index(request):
    return render(request, 'student/index.html')

# def student_page(request):
#     return render(request,'student/student.html')

def student_page(request):
    print(request.POST)
    print(request.FİLES)
    form = StudentForm()
    context = {
        "form": form
    }
    return render(request,"student/student.html",context)