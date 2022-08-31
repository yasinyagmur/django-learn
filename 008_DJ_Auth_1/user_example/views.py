from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
    #    register olduktan sonra login yapıyor
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password1")
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    #     return redirect('home')
    # else:
    #     form = UserCreationForm()
    
    # context = {
    #     'form': form
    # }
    
    # return render(request, "registration/register.html", context)

        return  redirect("login")
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)