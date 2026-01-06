from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('login')

    return render(request, 'users/signup.html')
    return render(request, 'users/signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'users/login.html')
