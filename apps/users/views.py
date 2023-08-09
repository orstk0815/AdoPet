from django.shortcuts import render, redirect

# Create your views here.


def user(request):
    return render(request, 'users/user.html')
