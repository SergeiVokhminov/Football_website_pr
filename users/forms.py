from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserAuthForm(AuthenticationForm):
    """Форма для входа пользователя на сайт."""

    email = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Введите пароль"}
        ),
        label="Пароль",
    )


class UserRegisterForm(UserCreationForm):
    """Форма регистрации пользователя на сайте."""

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )

    def clean_email(self):
        """Проверка электронной почты."""

        email_address = self.cleaned_data.get("email")
        if User.objects.filter(email=email_address).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже зарегистрирован!")
        return email_address
