from django.urls import path
from .views import EmployeeView, EmployeListView, EmployeeUpdate, EmployeeDelete


urlpatterns = [
    path("a/", EmployeeView.as_view(), name="employee_url"),
    path("b/", EmployeListView.as_view(), name='employee_list_url'),
    path("c/<int:pk>/", EmployeeUpdate.as_view(), name='employee_update_url'),
    path("d/<int:pk>/", EmployeeDelete.as_view(), name='employee_delete_url')
]