from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Поля для модели пользователя в базе данных."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    token = models.CharField(
        max_length=100, verbose_name="Токен пользователя", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.last_name} {self.first_name}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
