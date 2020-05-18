from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        # Login User
        return
    context = {

    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    return redirect('index')


def register(request):
    if request.method == 'POST':
        # Register User
        messages.error(request, 'Testing error message')
        return redirect('register')

    else:
        context = {

        }
        return render(request, 'accounts/register.html', context)


def dashboard(request):
    context = {

    }
    return render(request, 'accounts/dashboard.html', context)
