from django.shortcuts import render

from Account.views import get_user, has_signed_in, not_signed_in_error
from Share.models import Post


def share(request, user_name):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    post_list = Post.objects.filter(user=user).order_by("-post_date")
    if request.method == "GET":
        context = {
            "title": "share",
            "user_name": user_name,
            "post_list": post_list,
        }
        return render(request, "share.html", context=context)


def post(request, user_name):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    post_list = Post.objects.filter(user=user).order_by("-post_date")
    if request.method == "GET":
        context = {
            "title": "share",
            "user_name": user_name,
            "post_list": post_list,
        }
        return render(request, "share_post.html", context=context)
    if request.method == "POST":
        post_text = request.POST.get("post_text")
        post_photo = request.POST.get("post_photo")
        if not post_text and not post_photo:
            context = {
                "title": "share",
                "user_name": user_name,
                "post_list": post_list,
                "error": "Sorry, cannot share an empty post"
            }
            return render(request, "share_post.html", context=context)
        Post.objects.create(user=user, post_text=post_text, post_photo=post_photo)
        post_list = Post.objects.filter(user=user).order_by("-post_date")
        context = {
            "title": "share",
            "user_name": user_name,
            "post_list": post_list,
        }
        return render(request, "share.html", context=context)