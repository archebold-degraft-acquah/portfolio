from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "app"

urlpatterns = [
    path("<str:user_name>/", views.user_portfolio, name="user_portfolio"),
    path("<str:user_name>/messages/", views.user_messages, name="user_messages"),
    path("<str:user_name>/reply_messages/<message_id>/", views.reply_messages, name="reply_messages"),
]
