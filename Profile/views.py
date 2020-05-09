from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Account.views import get_user, not_signed_in_error
from Account.forms import UserForm
from Chat.models import Friend
from Share.models import Post


@csrf_exempt
def profile(request, user_name):
    user = get_user(user_name, request)
    if not user:
        return not_signed_in_error(request)

    if request.method == 'GET':
        posts = Post.objects.filter(user=user).count()
        friends = Friend.objects.filter(user=user).count()

        context = {
            "title": "profile",
            "user_name": user_name,
            "user_photo": user.photo.url,
            "posts": posts,
            "friends": friends,
        }
        return render(request, "profile.html", context=context)
    elif request.method == 'POST':
        photo = request.FILES
        user_form = UserForm(request.POST, photo)
        if user_form.is_valid():
            user.photo = user_form.cleaned_data['photo']
            user.save()
        data = {
            "photo": user.photo.url
        }
        return JsonResponse(data)