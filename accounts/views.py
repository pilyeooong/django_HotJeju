from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout
from .forms import LoginForm

def account_join(request):
    if request.method=="POST":
        if request.POST["password1"]==request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password1"])
            auth.login(request,user)
            return redirect('/')
        return render(request, 'account/join.html')
    return render(request, 'account/join.html')

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(username=name, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})


def logout(request):
    django_logout(request)
    return redirect('/')


