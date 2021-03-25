from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from MyHospital.service_provider import hms_service_provider


@login_required(redirect_field_name='next')
def profile_view(request):
    groups = request.session.get('groups')
    if 'Patient' in groups:
        user_id = request.user.id
        patient = hms_service_provider.patient_management_service().get_details_by_user(user_id)

        context = {
            # 'patient_name': patient.username,

        }
        return render(request, 'profile.html', context)

    elif 'DepartmentHead' in groups:
        user_id = request.user.id
        department_head = hms_service_provider.department_head_management_service().get_details_by_user(user_id)
        context = {
            'department_head': department_head
        }
        return render(request, 'departmentheadprofile.html', context)

    else:
        return HttpResponse('INVALID GROUP')
