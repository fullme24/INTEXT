from django.http import HttpResponse
from django.shortcuts import render

# from .models import People

def JobDashboardTemplate(request) :
    return render(request, 'job/job_name_dashboard.html')

def companyListingTemplate(request) :
    return render(request, 'job/listing_company.html')

def recruiterListingTemplate(request) :
    return render(request, 'job/listing_recruiter.html')

def JobSearchTemplate(request) :
    return render(request, 'job/jobsearch.html')

def JobDescriptionTemplate(request) :
    return render(request, 'job/description.html')

def addTemplate(request):
    return render(request, 'job/add_job_listing.html')

def applyTemplate(request):
    return render(request, 'job/apply.html')

def submitTemplate(request):
    return render(request, 'job/submit.html')

def offerTemplate(request):
    return render(request, 'job/offer.html')

def jobSavedTemplate(request):
    return render(request, 'job/saved.html')
