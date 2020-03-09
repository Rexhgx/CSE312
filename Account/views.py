from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .models import User


@csrf_protect
def sign_in(request):
    if request.method == "GET":
        return render(request, "sign-in.html")
    if request.method == "POST":
        # try:
        #     User.objects.get(u_name=request.GET['username'], u_password=request.GET['password'])
        # except User.DoesNotExist:
        #     error_message = "Sorry! You may enter the wrong username or wrong password"
        #     return render(request, 'sign-in.html', {'error_message': error_message})
        return redirect(reverse('Account:chat'))


@csrf_protect
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    if request.method == 'POST':
        # u_name = request.POST['username']
        # u_password = request.POST['password']
        # user = User.objects.filter(u_name=u_name).first()
        # if user:
        #     return render(request, 'Account/signupgoing.html', {'error_message': "The user already exists."})
        # User.objects.create(u_name=u_name, u_password=u_password)
        # response = redirect(reverse('Account:sign_up_success'))
        return redirect(reverse('Account:sign_in'))


def chat(request):
    return render(request, "chat.html", context={"title": chat})


def share(request):
    return render(request, "share.html", context={"title": share})


def profile(request):
    return render(request, "profile.html", context={"title": profile})