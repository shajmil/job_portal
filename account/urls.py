from django.urls import path
from account import views

app_name = "account"

urlpatterns = [

    path('employee/register/', views.employee_registration, name='employee-registration'),
    path('employer/register/', views.employer_registration, name='employer-registration'),
    path('profile/edit/<int:id>/', views.employee_edit_profile, name='edit-profile'),
    path('upload-resume/<int:id>/', views.resume_page, name='resume-page'),
    path('job-resume/', views.upload_job_resume, name='job-resume'),
    
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
