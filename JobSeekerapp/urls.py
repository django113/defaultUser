from django.urls import path
from . import views
from .views import JobSeeker_detail, JobSeeker_edit

app_name = 'dashboard'

urlpatterns = [

    path('', views.JobSeekerregister, name='Register_JobSeeker'),

    path('JobSeeker/detail/<slug:slug>/', JobSeeker_detail,
         name='dashboard-JobSeeker-detail'),
    path('JobSeeker/edit/<slug:slug>/', JobSeeker_edit,
         name='dashboard-JobSeeker-edit'),

]
