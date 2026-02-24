from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from users.models import User


class Command(BaseCommand):
    """Класс создания пользователя-администратора и генерации токена."""

    def handle(self, *args, **options):
        """Метод создания пользователя-администратора."""

        user = User.objects.create(email="admin@test.ru")
        user.set_password("0admin0")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        # Генерация уникального токена
        token = None
        while not token:
            candidate = get_random_string(64)
            if not User.objects.filter(token=candidate).exists():
                token = candidate

        user.token = token
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Пользователь-администратор с электронной почтой {user.email} успешно создан!"
            )
        )
