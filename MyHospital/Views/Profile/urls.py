from django.urls import path
from MyHospital.Views.Profile import profile_view

urlpatterns = [
    path('profile/', profile_view.profile_view, name='profile'),

]