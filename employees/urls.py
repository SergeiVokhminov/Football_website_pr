from django.urls import path

from employees.apps import EmployeesConfig

from employees.views import (
    EmployeeCreateView,
    EmployeeDeleteView,
    EmployeeDetailsView,
    EmployeeInfoView,
    EmployeeListView,
    EmployeeUpdateView,
)

app_name = EmployeesConfig.name

urlpatterns = [
    path("employee/create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("employee/info/<int:pk>/", EmployeeInfoView.as_view(), name="employee_info"),
    path("employee/list/", EmployeeListView.as_view(), name="employee_list"),
    path("employee/detail/<int:pk>/", EmployeeDetailsView.as_view(), name="employee_detail"),
    path("employee/update/<int:pk>/", EmployeeUpdateView.as_view(), name="employee_update"),
    path("employee/delete/<int:pk>/", EmployeeDeleteView.as_view(), name="employee_delete"),
]
