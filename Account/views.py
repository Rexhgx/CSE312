from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from . models import User
from rest_framework.views import APIView


def homepage(request):
    return render(request, 'Account/homepage.html')


def sign_in(request):
    try:
        print(request )
        user = User.objects.get(u_name=request.GET['username'], u_password=request.GET['password'])
    except User.DoesNotExist:
        error_message = "Sorry! You may enter the wrong username or wrong password"
        return render(request, 'Account/homepage.html', {'error_message': error_message})
    response = redirect(reverse('Account:welcome', args=(user.u_name,)))
    return response


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'Account/homepage.html')
    if request.method == 'POST':
        u_name = request.POST['username']
        u_password = request.POST['password']
        user = User.objects.filter(u_name=u_name).first()
        if user:
            return render(request, 'Account/signupgoing.html', {'error_message': "The user already exists."})
        User.objects.create(u_name=u_name, u_password=u_password)
        response = redirect(reverse('Account:sign_up_success'))
        return response


def sign_up_going(request):
    return render(request, 'Account/signupgoing.html')


def sign_up_success(request):
    return render(request, 'Account/signupsuccess.html')


def welcome(request, username):
    context = {
        'username': username
    }
    return render(request, 'Account/user.html', context=context)


def log_out(request):
    return redirect(reverse('Account:homepage'))