from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from . models import User


def homepage(request):
    return render(request, 'Account/homepage.html')


def sign_in(request):
    try:
        user = User.objects.get(u_name=request.GET['username'], u_password=request.GET['password'])
    except User.DoesNotExist:
        return render(request, 'Account/homepage.html', {'error_message': "The user does not exist."})
    return HttpResponseRedirect(reverse('Account:welcome', args=(user.u_name,)))


def sign_up(request):
    u_name = request.POST['username']
    u_password = request.POST['password']
    user = User.objects.filter(u_name=u_name).first()
    if user:
        return render(request, 'Account/signupgoing.html', {'error_message': "The user already exists."})
    User.objects.create(u_name=u_name,u_password=u_password)
    return HttpResponseRedirect(reverse('Account:sign_up_success'))


def sign_up_going(request):
    return render(request, 'Account/signupgoing.html')


def sign_up_success(request):
    return render(request, 'Account/signupsuccess.html')


def welcome(request, user_name):
    return HttpResponse("Welcome, %s!" % user_name)


