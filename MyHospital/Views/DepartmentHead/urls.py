from django.urls import path
from MyHospital.Views.DepartmentHead import view

urlpatterns = [
    path('register_department_head', view.create_department_head, name='register_department_head'),
    path('list_department_head', view.list_department_head, name='list_department_head'),
    path('department_head_details', view.department_head_detail, name='department_head_detail'),
    path('edit_department_head', view.edit_department_head, name='edit_department_head'),
]