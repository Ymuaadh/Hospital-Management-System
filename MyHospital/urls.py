"""MyHospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include

from MyHospital.Views.Login import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view.login_get, name='home'),
    path('login/', include('MyHospital.Views.Login.urls')),
    path('patient/', include('MyHospital.Views.Patient.urls')),
    path('department_head/', include('MyHospital.Views.DepartmentHead.urls')),
    path('appointment/', include('MyHospital.Views.Appointment.urls')),
    path('doctor/', include('MyHospital.Views.Doctor.urls')),
    path('profile/', include('MyHospital.Views.Profile.urls'))


]
