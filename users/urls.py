from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UserLoginView,
    UserRegisterView,
    EmailVerifyView,
    RegistrationSuccessView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/", UserLoginView.as_view(template_name="users/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(next_page="home_pages:home"), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("email_confirm/<str:token>/", EmailVerifyView.as_view(), name="email_verification"),

    path("register-success", RegistrationSuccessView.as_view(), name="register_success")
]
