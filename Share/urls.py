from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Share import views

app_name = 'Share'
urlpatterns = [
    path('<user_name>/share/', views.share, name="<user_name>/share"),
    path('<user_name>/share/post', views.post, name="<user_name>/share/post"),
    path('<user_name>/share/<post_id>/like', views.like, name="<user_name>/share/<post_id>/like"),
    path('<user_name>/share/<post_id>/comment', views.comment, name="<user_name>/share/<post_id>/comment"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
