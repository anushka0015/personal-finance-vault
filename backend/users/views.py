from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Personal Finance Vault")
def signup(request):
    return render(request, 'users/signup.html')

# Create your views here.
