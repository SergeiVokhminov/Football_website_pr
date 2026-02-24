from django import forms

from users.models import User


def validate_email_address(email_address, instance=None):
    """Проверка электронной почты на уникальность."""

    if User.objects.filter(email=email_address).exclude(pk=instance.pk).exists():
        raise forms.ValidationError("Этот адрес электронной почты уже зарегистрирован!")
    return email_address


def validate_phone_number(phone_number):
    """Проверка телефонного номера на допустимые значения."""

    if phone_number and not phone_number.isdigit():
        raise forms.ValidationError("Номер телефона должен содержать только цифры.")
    return phone_number
