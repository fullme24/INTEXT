from django.urls import path
from .views import JobDashboardTemplate, JobDescriptionTemplate, addTemplate, applyTemplate, companyListingTemplate, JobSearchTemplate, jobSavedTemplate, offerTemplate, recruiterListingTemplate, submitTemplate

urlpatterns = [
    path("", JobSearchTemplate, name="jobsearchtemplate"),
    path("dashboard/", JobDashboardTemplate, name="jobdashboardtemplate"),
    path("listing/", companyListingTemplate, name="companylistingtemplate"),
    path("description/", JobDescriptionTemplate, name="descriptiontemplate"),
    path("listing/recruiter", recruiterListingTemplate, name="recruiterlistingtemplate"),
    path("add/", addTemplate, name="addjoblisting"),
    path("apply/", applyTemplate, name="applytemplate"),
    path("submit/", submitTemplate,name="submittemplate"),
    path("offer/", offerTemplate,name="offertemplate"),
    path("save/", jobSavedTemplate,name="savetemplate"),

] 