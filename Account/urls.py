from django.urls import path
from Account import views

app_name = 'Account'
urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('<user_name>/chat/', views.chat, name='<user_name>/chat'),
    path('<user_name>/profile/', views.profile, name="<user_name>/profile"),
]