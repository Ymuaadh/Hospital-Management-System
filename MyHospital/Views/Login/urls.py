from django.urls import path
from MyHospital.Views.Login import login_view

urlpatterns = [
    path('login_post', login_view.login_post, name='login'),
    path('', login_view.log_out, name='logout')
]