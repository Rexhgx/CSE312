from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from Account.models import User
from Account.views import get_user, not_signed_in_error

from Share.views import remove_danger_symbols

from Chat.models import Friend, Message, Room


def chat(request, user_name):
    user = get_user(user_name, request)
    if not user:
        return not_signed_in_error(request)
    friends = Friend.objects.filter(user=user).order_by('-id')
    context = {
        "title": "chat",
        "user_name": user_name,
        "friends": friends,
        "user_photo": user.photo.url,
    }
    return render(request, "chat.html", context=context)


@csrf_exempt
def friend(request, user_name):
    if request.method == 'POST':
        user = get_user(user_name, request)
        if not user:
            return not_signed_in_error(request)

        friend_name = request.POST.get("username")

        error = ""
        if friend_name == user_name:
            # When the friend's name is the current user's name
            error = "Sorry, you cannot add yourself as a friend."
        elif Friend.objects.filter(friend_name=friend_name, user_id=user.id).count():
            # When the friend already exists
            error = "Sorry, you have added this friend."
        try:
            friend = User.objects.get(username=friend_name)
        except:
            # When the friend does not exist
            error = "Sorry, please enter a valid username"

        if error:
            data = {"error": error}
            return JsonResponse(data)
        else:
            # Add friends
            Friend.objects.create(friend_name=friend_name, user=user)
            Friend.objects.create(friend_name=user_name, user=friend)

            # Create a room for the user and each friend
            Room.objects.create(user_one=user_name, user_two=friend_name)

            data = {"friend_name": friend_name}
            return JsonResponse(data)


@csrf_exempt
def messages(request, user_name, friend_name):
    user = get_user(user_name, request)
    if not user:
        return not_signed_in_error(request)

    friend = get_object_or_404(Friend, friend_name=friend_name, user=user)

    if request.method == 'GET':
        friend.last_message_color = "#5c5c5c"
        friend.save()

        response = {"messages": [], "room": None}

        # Get messages between the user and a friend
        messages = Message.objects.filter(
                Q(sender_name=user_name, receiver_name=friend_name) |
                Q(sender_name=friend_name, receiver_name=user_name)
        ).order_by("id")
        for message in messages:
            response["messages"].append({
                "sender_name": message.sender_name,
                "receiver_name": message.receiver_name,
                "content": message.content
            })

        # Get the room between the user and a friend
        room = Room.objects.get(
            Q(user_one=user_name, user_two=friend_name) |
            Q(user_one=friend_name, user_two=user_name)
        )
        response["room"] = room.id

        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        content = remove_danger_symbols(request.POST.get("content"))

        # Store the last message between the user and the friend
        friend.last_message = content
        friend.last_message_color = "#5c5c5c"
        friend.save()

        temp_user = User.objects.get(username=friend_name)
        temp_friend = get_object_or_404(Friend, friend_name=user_name, user=temp_user)
        temp_friend.last_message = content
        temp_friend.save()

        message = Message.objects.create(
            friend=friend,
            sender_name=user_name,
            receiver_name=friend_name,
            content=content)
        data = {
            "sender_name": message.sender_name,
            "receiver_name": message.receiver_name,
            "content": message.content
        }
        return JsonResponse(data)

