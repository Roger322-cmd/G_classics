from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, register, profile

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="core:home"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
