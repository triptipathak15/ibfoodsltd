from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

total = 20


def home(request):
    return render(request, "home.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Username/password is incorrect")
    return render(request, "registration/login.html", {})


def logoutPage(request):
    logout(request)
    return redirect('/login')