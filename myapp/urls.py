from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('job-list/',views.job_list,name='job-list'),
    path('job-detail/',views.job_detail,name='job-detail'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('logout/',views.logout,name='logout'),
    path('company-index/',views.company_index,name='company-index'),
    path('company-about/',views.company_about,name='company-about'),
    path('post-job/',views.post_job,name='post-job'),
    path('company-profile/',views.company_profile,name='company-profile'),
    path('employe-profile/',views.employe_profile,name='employe-profile'),
    path('delete-post/',views.delete_post,name='delete-post'),
    path('employe-appointment/',views.employe_appointment,name='employe-appointment'),
    path('apply-now/<int:pk>/',views.apply_now,name='apply-now'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
    
]