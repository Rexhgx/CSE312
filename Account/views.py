from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .models import User

"""
    Helper function
"""


def get_user(user_name, request=None):
    try:
        # Check user exists
        user = User.objects.get(user_name=user_name)
    except:
        return False
    else:
        # Check user has signed in
        token = request.COOKIES.get("token")
        if str(token) == str(user.user_token):
            return user
        else:
            return False


def not_signed_in_error(request):
    error = "Sorry! Looks like you have not signed in yet."
    return render(request, 'sign-in.html', {'error': error})


"""
    View function
"""


def redirect_to_sign_in(request):
    return redirect(reverse('Account:sign_in'))


@csrf_protect
def sign_in(request):
    if request.method == "GET":
        token = request.COOKIES.get("token")
        if token:
            # Check user has signed in and not signed out yet
            try:
                user = User.objects.get(user_token=token)
            except:
                # if token is invalid, stay in the sign in page
                return render(request, "sign-in.html")
            else:
                # if token is valid, redirect to the chat page
                return redirect(reverse('Chat:<user_name>/chat', args=[user.user_name]))
        else:
            return render(request, "sign-in.html")
    if request.method == "POST":
        try:
            # Check if username and password are correct
            user = User.objects.get(user_name=request.POST.get('username'), user_password=request.POST.get('password'))
        except User.DoesNotExist:
            # If not, stay in the "sign-in page" with a error
            error = "Sorry! Please enter the correct username and password"
            return render(request, 'sign-in.html', {'error': error})
        else:
            # If yes, redirect to "chat" page
            response = redirect(reverse('Chat:<user_name>/chat', args=[user.user_name]))
            response.set_cookie("token", user.user_token)
            return response


@csrf_protect
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')

        # Check username and password are entered correctly
        if len(user_name) > 16 or len(user_password) > 16:
            error = "Username or password is too long (maximum is 16 characters)"
            return render(request, 'sign-up.html', {'error': error})

        elif len(user_name) == 0 or len(user_password) == 0:
            error = "Username or password is empty"
            return render(request, 'sign-up.html', {'error': error})

        if User.objects.filter(user_name=user_name).count():
            error = "The user already exists."
            return render(request, 'sign-up.html', {'error': error})

        User.objects.create(user_name=user_name, user_password=user_password)
        return redirect(reverse('Account:sign_in'))


def sign_out(request, user_name):
    user = get_user(user_name, request)
    if not user:
        return not_signed_in_error(request)

    response = redirect(reverse('Account:sign_in'))
    # delete token
    response.delete_cookie("token")
    return response
