from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Applications, Person, PersonType, MinorityType, CompanyEmployee, Company, CategoryType, CompanySize, JobListings, JobOffers, Resumes, SavedJobs, SkillLevel, Skills, Applications, Resumes


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