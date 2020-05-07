from django.urls import path
from Profile import views

app_name = 'Profile'
urlpatterns = [
    path('<user_name>/profile', views.profile, name="<user_name>/profile"),
]