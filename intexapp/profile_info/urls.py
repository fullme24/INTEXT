from django.urls import path
from .views import ProfileTemplate,CompanyProfileTemplate, RecruiterProfileTemplate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", ProfileTemplate, name="profiletemplate"),
    path("company/", CompanyProfileTemplate, name="companyprofiletemplate"),
     path("recruiter/", RecruiterProfileTemplate, name="recruiterprofiletemplate"),
] 