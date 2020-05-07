from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import re_path

from Chat.consumers import ChatConsumer
import Share.routing
from Share.consumers import ShareConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/(?P<room>\w+)/$', ChatConsumer),
            re_path(r'ws/(?P<user_name>\w+)/share/$', ShareConsumer)
        ])
    )
})