from django.http import HttpResponse
from django.shortcuts import render
from login.models import JobListings, Company, CompanySize, CompanyEmployee, Person

# from .models import People

def JobDashboardTemplate(request) :
    return render(request, 'job/job_name_dashboard.html')

def companyListingTemplate(request) :
    return render(request, 'job/listing_company.html')

def recruiterListingTemplate(request) :
    return render(request, 'job/listing_recruiter.html')

def JobSearchTemplate(request) :
    companyData = Company.objects.all()

    context = {
        'company' : companyData,
    }

    return render(request, 'job/jobsearch.html', context)

def job_listings_per_comp(request):

    company = request.POST['company_id']

    companyData = Company.objects.get(companyName = company)

    fakeComapnyID = companyData.companyID

    jobData = JobListings.objects.filter(companyID = fakeComapnyID)

    context = {
        
        'jobs' : jobData,
        'company' : companyData,

    }

    print(context['jobs'])
    
    return render(request, 'job/listing_company.html', context)

def JobDescriptionTemplate(request, job_listing) :
    jobData = JobListings.objects.get(jobListingID = job_listing)
    fakeCompanyID = jobData.companyID
    companyData = Company.objects.get(companyID=fakeCompanyID.companyID)
    sizeData = CompanySize.objects.get(companySizeID = companyData.companySizeID_id)
    empData = CompanyEmployee.objects.values('personID')[:1]
    fakePersonID = empData[0]['personID']
    print(fakePersonID)
    personData = Person.objects.get(personID=fakePersonID)
    print(personData.phone)
    
    context = {
        'job' : jobData,
        'company' : companyData,
        'size' : sizeData,
        'emp' : empData,
        'person' : personData
    }
    
    return render(request, 'job/description.html', context)

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
