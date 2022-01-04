from django.urls import include, path

from . import views

urlpatterns = [
    path("", include("common.urls")),
    path("admins/", views.admin_api_view, name="admins"),
    path("users/", views.users_api_view, name="users"),
]
