from django import forms

from employees.models import Employee
from users.validators import validate_email_address, validate_phone_number


class EmployeeForm(forms.ModelForm):
    """Форма представления пользователя."""

    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)


class EmployeeUpdateForm(forms.ModelForm):
    """Форма обновления данных пользователя."""

    class Meta:
        model = Employee
        fields = (
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "position",
            "department",
            "phone_number",
            "condition",
            "address",
            "avatar",
        )
        widgets = {
            'condition': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap стиль
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите фамилию"}
        )
        self.fields["patronymic"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите отчество"}
        )
        self.fields["position"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите должность"}
        )
        self.fields["department"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите структурное подразделение"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите номер телефона (только цифры)",
            }
        )
        self.fields["condition"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите статус сотрудника"}
        )
        self.fields["address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес регистрации"}
        )
        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите фотографию"}
        )

    def clean_email(self):
        """Проверка электронной почты."""

        email_address = self.cleaned_data.get("email")
        return validate_email_address(email_address, self.instance)

    def clean_phone_number(self):
        """Проверка телефонного номера."""

        phone_number = self.cleaned_data.get("phone_number")
        return validate_phone_number(phone_number)
