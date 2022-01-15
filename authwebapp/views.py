from contextlib import redirect_stderr, redirect_stdout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from authwebapp.apps import AuthwebappConfig


def home(request):
    return render(request,'home.html')

def fileupload(request):
    return render(request,'fileupload.html')

def showdata(request):
    return render(request,'showdata.html')

def login1(request):
    if request.method == 'POST':

        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user = authenticate(username=username1, password=password1)

        if user is None:
            return redirect_stderr('home')
        else:
            login(request, user)
            return render(request, 'fileupload.html')

    else:
        return render(request,'home.html')

def logout_view(request):
    logout(request)

# Create your views here.
