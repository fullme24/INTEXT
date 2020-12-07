from django.urls import path
from .views import ProfileTemplate,CompanyProfileTemplate, RecruiterProfileTemplate

urlpatterns = [
    path("", ProfileTemplate, name="profiletemplate"),
    path("company/", CompanyProfileTemplate, name="companyprofiletemplate"),
     path("recruiter/", RecruiterProfileTemplate, name="recruiterprofiletemplate"),
] 