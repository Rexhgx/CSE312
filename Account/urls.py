from django.urls import path
from Account import views

app_name = 'Account'
urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('chat/', views.chat, name='chat'),
    path('share/', views.share, name="share"),
    path('share/', views.profile, name="profile"),
]