from cgitb import html
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def home(request):
#     print(request)
#     print(request.method)
#     print(request.COOKIES)
#     print(request.path)
#     # print(request.user) migrate komutundan sonra çalışır
#     print(request.META)

#     html = "Hello Fs Cohort"
#     return HttpResponse(html)
def home(request):
    context = {
        'caption': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "fsApp/index.html", context)
