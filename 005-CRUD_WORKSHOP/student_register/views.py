from django.shortcuts import render, redirect
from .forms import StudentFrom
from .models import Student
# Create your views here.

def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)


def student_add_update(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentFrom()
        else:
            student = Student.objects.get(pk=id)
            form = StudentFrom(instance=student)
            return render(request, "student_register/student_form.html", {'form':form})

