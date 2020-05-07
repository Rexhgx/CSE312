from django.shortcuts import render

from Account.views import get_user, not_signed_in_error
from Chat.models import Friend
from Share.models import Post


def profile(request, user_name):
    user = get_user(user_name, request)
    if not user:
        return not_signed_in_error(request)

    posts = Post.objects.filter(user=user).count()
    friends = Friend.objects.filter(user=user).count()

    context = {
        "title": "profile",
        "user_name": user_name,
        "posts": posts,
        "friends": friends,
    }
    return render(request, "profile.html", context=context)
