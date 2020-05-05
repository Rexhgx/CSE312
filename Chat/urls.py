from django.urls import path
from Chat import views

app_name = 'Chat'
urlpatterns = [
    path('<user_name>/chat', views.chat, name="<user_name>/chat"),
    path('<user_name>/friend', views.friend, name="<user_name>/friend"),
]