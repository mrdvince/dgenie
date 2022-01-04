from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("user/", views.user_api_view, name="user"),
    path("logout/", views.logout, name="logout"),
    path("user/info/", views.user_info, name="profile"),
    path("user/update-password/", views.user_password, name="update-password"),
]
