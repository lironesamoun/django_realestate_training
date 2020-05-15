from django.shortcuts import render, redirect


def login(request):
    context = {

    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    return redirect('index')


def register(request):
    context = {

    }
    return render(request, 'accounts/register.html', context)


def dashboard(request):
    context = {

    }
    return render(request, 'accounts/dashboard.html', context)
