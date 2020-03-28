from django.shortcuts import render

from Account.views import get_user, has_signed_in, not_signed_in_error


def share(request, user_name):
    if request.method == "GET":
        user = get_user(user_name)
        if not user:
            return not_signed_in_error(request)
        check_has_signed_in = has_signed_in(request, user)
        if not check_has_signed_in:
            return not_signed_in_error(request)
        context = {
            "title": "share",
            "user_name": user_name,
        }
        return render(request, "share.html", context=context)
    if request.method == "POST":
        pass