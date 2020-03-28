from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .models import User


def get_user(user_name):
    try:
        user = User.objects.get(user_name=user_name)
    except:
        return False
    return user


def has_signed_in(request, user):
    token = request.COOKIES.get("token")
    return str(token) == str(user.user_token)


def not_signed_in_error(request):
    error = "Sorry! Looks like you have not signed in yet."
    return render(request, 'sign-in.html', {'error': error})

@csrf_protect
def sign_in(request):
    if request.method == "GET":
        return render(request, "sign-in.html")
    if request.method == "POST":
        try:
            # Check if username and password are correct
            user = User.objects.get(user_name=request.POST.get('username'), user_password=request.POST.get('password'))
        except User.DoesNotExist:
            # If not, route to "sign-in page" with a error
            error = "Sorry! Please enter the correct username and password"
            return render(request, 'sign-in.html', {'error': error})
        else:
            # If yes, route to "chat" page
            response = redirect(reverse('Account:<user_name>/chat', args=[user.user_name]))
            response.set_cookie("token", user.user_token)
            return response


@csrf_protect
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        if len(user_name) > 16 or len(user_password) > 16:
            error = "Username or password is too long (maximum is 16 characters)"
            return render(request, 'sign-up.html', {'error': error})
        elif len(user_name) == 0 or len(user_password) == 0:
            error = "Username or password is empty"
            return render(request, 'sign-up.html', {'error': error})
        if User.objects.filter(user_name=user_name).count():
            # Username has already been registered
            error = "The user already exists."
            return render(request, 'sign-up.html', {'error': error})
        # Username has not been registered
        user = User.objects.create(user_name=user_name, user_password=user_password)
        return redirect(reverse('Account:sign_in'))


def chat(request, user_name):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    context = {
        "title": "chat",
        "user_name": user_name,
    }
    return render(request, "chat.html", context=context)


def profile(request, user_name):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    if not user or not check_has_signed_in:
        error = "Sorry! Looks like you have not signed in yet."
        return render(request, 'sign-in.html', {'error': error})
    context = {
        "title": "profile",
        "user_name": user_name,
    }
    return render(request, "profile.html", context=context)
