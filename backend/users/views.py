from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # create user
        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('home')

    return render(request, 'users/signup.html')
