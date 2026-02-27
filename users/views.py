import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    CreateView,
    TemplateView,
)

from employees.models import Employee
from users.forms import UserAuthForm, UserRegisterForm
from users.models import User


class UserLoginView(LoginView):
    """Контроллер для входа на сайт."""

    model = User
    form_class = UserAuthForm
    template_name = "users/login.html"  # Указываем путь к шаблону для входа
    success_url = reverse_lazy(
        "home_pages:home"
    )  # Указываем URL, на который будет перенаправлен пользователь после успешного входа
    redirect_authenticated_user = (
        True  # Перенаправлять аутентифицированных пользователей
    )

class UserRegisterView(CreateView):
    """Контроллер регистрации профиля."""

    model = User
    form_class = UserRegisterForm  # Указываем какую форму использовать для регистрации
    template_name = "users/register.html"  # Указываем путь к шаблону для регистрации
    success_url = reverse_lazy(
        "users:register_success"
    ) # Указываем URL, на который будет перенаправлен пользователь после успешной регистрации

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # Деактивируем до подтверждения почты
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение регистрации на сайте.",
            message=f"Привет {user.first_name}! Для активации Вашего аккаунта перейдите по ссылке: {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email,],
        )
        return super().form_valid(form)


class EmailVerifyView(View):
    """Класс для подтверждения почты и автоматического создания записи сотрудника."""

    def get(self, request, token):
        try:
            user = User.objects.get(token=token)
            user.is_active = True
            user.is_verified = True
            user.save()

            # Автоматическое создание сотрудника
            Employee.objects.get_or_create(
                email=user.email,
                defaults={'token': user.token, 'user_account': user}
            )
            return redirect(reverse("users:login"))
        except User.DoesNotExist:
            return redirect(reverse("users:register"))


class RegistrationSuccessView(TemplateView):
    template_name = "users/register_success.html"
