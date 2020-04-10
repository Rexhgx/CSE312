from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Account.views import get_user, has_signed_in, not_signed_in_error
from Share.forms import PostForm
from Share.models import Post, Like, Comment


def share(request, user_name):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    post_list = Post.objects.filter(user=user).order_by("-post_date")
    like_list = Like.objects.all()
    comment_list = Comment.objects.all()
    if request.method == "GET":
        context = {
            "title": "share",
            "user_name": user_name,
            "post_list": post_list,
            "like_list": like_list,
            "comment_list": comment_list,
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
        post_photo = request.FILES
        post_form = PostForm(request.POST, post_photo)
        if not post_text and not post_photo:
            context = {
                "title": "share",
                "user_name": user_name,
                "post_list": post_list,
                "error": "Sorry, cannot share an empty post"
            }
            return render(request, "share_post.html", context=context)
        if post_form.is_valid():
            Post.objects.create(user=user, post_text=post_text, post_photo=post_form.cleaned_data['post_photo'])
        else:
            Post.objects.create(user=user, post_text=post_text)
        return redirect(reverse('Share:<user_name>/share', args=[user.user_name]))


def like(request, user_name, post_id):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    if request.method == "POST":
        try:
            Like.objects.get(liker=user_name, post_id=post_id)
            return HttpResponse("Exist")
        except:
            new_like = Like.objects.create(liker=user_name, post_id=post_id)
            data = {
                "post_id": post_id,
                "like_id": new_like.id,
                "liker": new_like.liker,
            }
            return JsonResponse(data)


def comment(request, user_name, post_id):
    user = get_user(user_name)
    if not user:
        return not_signed_in_error(request)
    check_has_signed_in = has_signed_in(request, user)
    if not check_has_signed_in:
        return not_signed_in_error(request)
    text = request.POST.get("text")
    if text:
        Comment.objects.create(commenter=user_name, comment_text=text, post_id=post_id)
        data = {
            "post_id": post_id,
            "commenter": user_name,
            "comment_text": text,
        }
        return JsonResponse(data)
    else:
        error = {
            "error": "error"
        }
        return JsonResponse(error)
