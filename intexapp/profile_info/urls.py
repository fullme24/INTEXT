from django.urls import path
from .views import ProfileTemplate,CompanyProfileTemplate, RecruiterProfileTemplate, employeeLookTemplate, get_infor_for_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", ProfileTemplate, name="profiletemplate"),
    path("company/", CompanyProfileTemplate, name="companyprofiletemplate"),
    path("recruiter/", RecruiterProfileTemplate, name="recruiterprofiletemplate"),
    path("employee_search/<int:personID>/<int:personTypeID>", employeeLookTemplate, name="employee_search"),
    path("get_infor_for_profile/<int:personID>/<int:personTypeID>", get_infor_for_profile, name="get_infor_for_profile"),
] 