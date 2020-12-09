from django.shortcuts import render
from . import views
import login.views
from login.models import Person

# Create your views here.
def ProfileTemplate(request) :
    return render(request, 'profile_info/myprofile.html')

def CompanyProfileTemplate(request) :
    return render(request, 'profile_info/companyprofile.html')

def RecruiterProfileTemplate(request) :
    return render(request, 'profile_info/recruiterprofile.html')