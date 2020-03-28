from django.urls import path
from Share import views

app_name = 'Share'
urlpatterns = [
    path('<user_name>/share/', views.share, name="<user_name>/share"),
]