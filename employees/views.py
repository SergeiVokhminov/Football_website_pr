from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from employees.models import Employee
from employees.forms import EmployeeForm, EmployeeUpdateForm


class AdminRequiredMixin(UserPassesTestMixin):
    """Проверка, является ли пользователь администратором."""

    def test_func(self):
        return self.request.user.is_staff


class EmployeeCreateView(AdminRequiredMixin, CreateView):
    """Контроллер добавления пользователя на сайт."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees:employee_list.html")


class EmployeeInfoView(UpdateView):
    """Контроллер просмотра профиля пользователя."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_info.html"
    success_url = reverse_lazy("home_page:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EmployeeListView(ListView):
    """Контроллер отображения списка пользователей сервиса."""

    model = Employee
    template_name = "employees/employee_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EmployeeDetailsView(DetailView):
    """Контроллер отображения профиля пользователя."""

    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_detail.html"


class EmployeeUpdateView(AdminRequiredMixin, UpdateView):
    """Контроллер обновления профиля пользователя."""

    model = Employee
    form_class = EmployeeUpdateForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("home_page:home")

    def form_valid(self, form):
        # Если email меняется в сотруднике, обновляем его и в связанном пользователе
        employee = form.save()
        if employee.user_account:
            employee.user_account.email = employee.email
            employee.user_account.save()
        return super().form_valid(form)


class EmployeeDeleteView(AdminRequiredMixin, DeleteView):
    """Контроллер удаления профиля пользователя."""

    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("home_page:home")

    def test_func(self):
        return (
            self.request.user.is_staff
        )  # Только администраторы могут удалять пользователей

    def get_object(self, queryset=None):
        return get_object_or_404(Employee, pk=self.kwargs["pk"])
