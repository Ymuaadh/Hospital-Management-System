from django.http import HttpRequest
from django.shortcuts import redirect, render

from MyHospital.dto.DepartmentHead import *
from MyHospital.service_provider import hms_service_provider


def create_department_head(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'DepartmentHead/registerhead.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            department_head = __get_attribute_from_request(request)
            if department_head.password == department_head.confirm_password:
                hms_service_provider.department_head_management_service().create_department_head(
                    department_head)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def list_department_head(request):
    department_head = hms_service_provider.department_head_management_service().list_department_head()
    context = {
        'title': 'List of Department Head',
        'department_head': department_head
    }
    return render(request, 'DepartmentHead/departmentheadlist.html', context)


def department_head_detail(request, department_head_id: int):
    department_head = hms_service_provider.department_head_management_service().department_head_details(
        department_head_id)
    context = {
        'department_head': department_head
    }
    return render(request, '', context)


def edit_department_head(request, department_head_id: int):
    department_head = hms_service_provider.department_head_management_service().department_head_details(
        department_head_id)
    context = {
        'department_head': department_head,
        "take_off_time": department_head.date_of_birth.strftime("%Y-%m-%d %H:%M:%S")
    }
    __edit_if_post_method(request, context, department_head_id)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, '', context)


def __edit_if_post_method(request, context, department_head_id: int):
    if request.method == 'POST':
        try:
            department_head = __get_attribute_from_request_for_edit(request)
            hms_service_provider.department_head_management_service().edit_department_head(department_head_id,
                                                                                           department_head)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request_for_edit(request):
    edit_department_head_dto = EditDepartmentHead()
    edit_department_head_dto.email = request.POST['email']
    edit_department_head_dto.address = request.POST['address']
    edit_department_head_dto.gender = request.POST['gender']
    edit_department_head_dto.date_of_birth = request.POST['date_of_birth']
    edit_department_head_dto.phone_number = request.POST['phone_number']
    edit_department_head_dto.first_name = request.POST['first_name']
    edit_department_head_dto.last_name = request.POST['last_name']
    return edit_department_head_dto


def __get_attribute_from_request(request: HttpRequest):
    register_department_head_dto = CreateDepartmentHead()
    register_department_head_dto.username = request.POST['username']
    register_department_head_dto.first_name = request.POST['first_name']
    register_department_head_dto.last_name = request.POST['last_name']
    register_department_head_dto.password = request.POST['password']
    register_department_head_dto.confirm_password = request.POST['confirm_password']
    register_department_head_dto.phone_number = request.POST['phone']
    register_department_head_dto.email = request.POST['email']
    register_department_head_dto.address = request.POST['address']
    register_department_head_dto.gender = request.POST['gender']
    register_department_head_dto.date_of_birth = request.POST['date_of_birth']
    return register_department_head_dto
