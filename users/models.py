import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Поля для модели пользователя в базе данных."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    token = models.CharField(
        max_length=100, verbose_name="Токен пользователя", unique=True, blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        """Переопределение сохранения для генерации токена при создании."""

        if not self.token:
            # Генерация безопасного токена
            self.token = secrets.token_urlsafe(32)
        super().save(*args, **kwargs)

    def __str__(self):
        """Метод для строкового представления объекта User."""

        return f"{self.email}"

    class Meta:
        """Мета-информация модели User."""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
