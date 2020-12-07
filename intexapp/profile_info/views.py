from django.shortcuts import render

# Create your views here.
def ProfileTemplate(request) :
    return render(request, 'profile_info/myprofile.html')

def CompanyProfileTemplate(request) :
    return render(request, 'profile_info/companyprofile.html')

def RecruiterProfileTemplate(request) :
    return render(request, 'profile_info/recruiterprofile.html')