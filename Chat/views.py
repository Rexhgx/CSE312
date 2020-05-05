from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Account.models import User
from Account.views import get_user, has_signed_in, not_signed_in_error

from Chat.models import Friend


def chat(request, user_name):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    friends = Friend.objects.filter(user=user)
    context = {
        "title": "chat",
        "user_name": user_name,
        "friends": friends,
    }
    return render(request, "chat.html", context=context)


@csrf_exempt
def friend(request, user_name):
    if request.method == 'POST':
        user = get_user(user_name)
        if not user:
            return not_signed_in_error(request)
        check_has_signed_in = has_signed_in(request, user)
        if not check_has_signed_in:
            return not_signed_in_error(request)

        friend_name = request.POST.get("username")

        error = ""
        if friend_name == user_name:
            # When the friend's name is the current user's name
            error = "Sorry, you cannot add yourself as a friend."
        elif User.objects.filter(user_name=friend_name).count() == 0:
            # When the friend does not exist
            error = "Sorry, please enter a valid username"
        elif Friend.objects.filter(friend_name=friend_name, user_id=user.id).count():
            # When the friend already exists
            error = "Sorry, you have added this friend."

        if error:
            data = {"error": error}
            return JsonResponse(data)
        else:
            f = Friend.objects.create(friend_name=friend_name, user=user)
            data = {"friend_name": f.friend_name}
            return JsonResponse(data)
