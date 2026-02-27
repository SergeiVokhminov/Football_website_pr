from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Поля в административной панели."""

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "position",
        "department",
        "phone_number",
    )
    list_filter = ("id", "first_name", "last_name")
    search_fields = ("email", "first_name", "last_name")
