from django.urls import path
from Account import views

app_name = 'Account'
urlpatterns = [
    path('', views.redirect_to_sign_in),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
]