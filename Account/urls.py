from django.urls import path
from Account import views

app_name = 'Account'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('welcome/<str:user_name>', views.welcome, name='welcome'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up_going/', views.sign_up_going, name='sign_up_going'),
    path('sign_up_success/', views.sign_up_success, name='sign_up_success'),
]