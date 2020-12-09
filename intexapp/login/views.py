from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Applications, Person, PersonType, MinorityType, CompanyEmployee, Company, CategoryType, CompanySize, JobListings, JobOffers, Resumes, SavedJobs, SkillLevel, Skills, Applications, Resumes

def profileView(request) :
        persondata = Person.objects.get(pk=1)
        companydata = Company.objects.get(pk=1)
        jobdata = JobListings.objects.get(pk=1)
        context = {
            "person" : persondata,
            "company": companydata,
            "job": jobdata
        }
        return render(request, 'login/myprofile.html',context)

def listingsView(request) :
        persondata = Person.objects.get(pk=1)
        companydata = Company.objects.get(pk=1)
        job1 = JobListings.objects.get(pk=1)
        job2 = JobListings.objects.get(pk=2)
        job3 = JobListings.objects.get(pk=3)
        job4 = JobListings.objects.get(pk=4)
        job5 = JobListings.objects.get(pk=5)
        job6 = JobListings.objects.get(pk=6)
        job7 = JobListings.objects.get(pk=7)
        job8 = JobListings.objects.get(pk=8)
        job9 = JobListings.objects.get(pk=9)
        job10 = JobListings.objects.get(pk=10)
        context = {
            "person" : persondata,
            "company": companydata,
            "job1": job1,
            "job2": job2,
            "job3": job3,
            "job4": job4,
            "job5": job5,
            "job6": job6,
            "job7": job7,
            "job8": job8,
            "job9": job9,
            "job10": job10
        }
        return render(request, 'login/listing_company.html',context)

def descriptionView1(request) :
        company1 = Company.objects.get(pk=1)
        job1 = JobListings.objects.get(pk=1)
        context = {
            "company1": company1,
            "job1": job1
        }
        return render(request, 'login/description/description1.html',context)

def descriptionView2(request) :
        company2 = Company.objects.get(pk=2)
        job2 = JobListings.objects.get(pk=2)
        context = {
            "company2": company2,
            "job2": job2
        }
        return render(request, 'login/description/description2.html',context)

def descriptionView3(request) :
        company3 = Company.objects.get(pk=3)
        job3 = JobListings.objects.get(pk=3)
        context = {
            "company3": company3,
            "job3": job3
        }
        return render(request, 'login/description/description3.html',context)


def descriptionView4(request) :
        company4 = Company.objects.get(pk=4)
        job4 = JobListings.objects.get(pk=4)
        context = {
            "company4": company4,
            "job4": job4
        }
        return render(request, 'login/description/description4.html',context)

def descriptionView5(request) :
        company5 = Company.objects.get(pk=5)
        job5 = JobListings.objects.get(pk=5)
        context = {
            "company5": company5,
            "job5": job5
        }
        return render(request, 'login/description/description5.html',context)

def descriptionView6(request) :
        company6 = Company.objects.get(pk=6)
        job6 = JobListings.objects.get(pk=6)
        context = {
            "company6": company6,
            "job6": job6
        }
        return render(request, 'login/description/description6.html',context)

def descriptionView7(request) :
        company7 = Company.objects.get(pk=7)
        job7 = JobListings.objects.get(pk=7)
        context = {
            "company7": company7,
            "job7": job7
        }
        return render(request, 'login/description/description7.html',context)

def descriptionView8(request) :
        company8 = Company.objects.get(pk=8)
        job8 = JobListings.objects.get(pk=8)
        context = {
            "company8": company8,
            "job8": job8
        }
        return render(request, 'login/description/description8.html',context)

def descriptionView9(request) :
        company9 = Company.objects.get(pk=9)
        job9 = JobListings.objects.get(pk=9)
        context = {
            "company9": company9,
            "job9": job9
        }
        return render(request, 'login/description/description9.html',context)


def descriptionView10(request) :
        company10 = Company.objects.get(pk=10)
        job10 = JobListings.objects.get(pk=10)
        context = {
            "company10": company10,
            "job10": job10
        }
        return render(request, 'login/description/description10.html',context)


def loginTemplate(request) :
    return render(request, 'login/login.html')

def CreateTemplate(request) :
    return render(request, 'login/create.html')

def CreateCompanyTemplate(request) :
    return render(request, 'login/create_company.html')


def CreatedLoginView(request):
    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_person = Person()

        #Store the data from the form to the new object's attributes (like columns)
        new_person.username = request.POST.get('user_name')
        new_person.password = request.POST.get('password')
        new_person.email = request.POST.get('email')
        new_person.phone = request.POST.get('phone_number')
        new_person.firstName = request.POST.get('first_name')
        new_person.lastName = request.POST.get('last_name')
        new_person.DOB = request.POST.get('birthdate')
        new_person.city = request.POST.get('city')
        new_person.state = request.POST.get('state')
        new_person.ZIP = request.POST.get('zip')

        new_person.save()

    return render(request, 'login/login.html')

def deleteTemplate(request):
    return render(request, 'login/delete.html')

def deleteView(request):
    person = Person.objects.filter(user_name=request.POST['user_name'], password=request.POST['password']).delete()
    return render(request, 'homepage/index.html')

def updateTemplate(request):
    return render(request, 'login/update.html')

def updateView(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        person = Person.objects.get(user_name=user_name, password=password)

        person.email = email
        person.phone = phone_number

        person.save()

    return render(request, 'login/login.html')

def loggedTemplate(request):
    if request.method == 'POST':
        sUser_name = request.POST.get('user_name')
        sPassword = request.POST.get('password')
        try:
            data = Person.objects.get(user_name=sUser_name, password=sPassword)
            greeting = 'Welcome Back!'
        except:
            data = 'No account matches. Please try again or Create a new account'
            greeting = 'Sorry!'
    
        content = {
                    'user' : data,
                    'greeting' : greeting

                }
    return render(request, 'login/logged_in.html', content)