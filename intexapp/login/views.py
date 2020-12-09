from blackcyberrecruiter.settings import DATABASES
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Applications, Person, PersonType, MinorityType, CompanyEmployee, Company, CategoryType, CompanySize, JobListings, JobOffers, Resumes, SavedJobs, SkillLevel, Skills, Applications, Resumes


def loginTemplate(request) :
    return render(request, 'login/login.html')

def CreateTemplate(request) :
    jobtype = CategoryType.objects.all()
    ethnicity = MinorityType.objects.all()
    return render(request, 'login/create.html', {'minorityTypes': ethnicity, 'jobtypes': jobtype})

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
        new_person.minorityTypeID = request.POST.get('ethnicity')

        new_person.save()

    return render(request, 'login/login.html')

def deleteTemplate(request):
    return render(request, 'login/delete.html')

def deleteView(request):
    person = Person.objects.filter(user_name=request.POST['user_name'], password=request.POST['password']).delete()
    return render(request, 'homepage/index.html')

def updateTemplate(request):
    ethnicity = MinorityType.objects.all()
    return render(request, 'login/update.html', {'minorityTypes': ethnicity})

def updateView(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        facebook = request.POST.get('facebook') 
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        aboutMe = request.POST.get('aboutMe')
        jobExperience = request.POST.get('jobExperience')
        ethnicity = request.POST.get('minorityType')
        ethnicityID = MinorityType.objects.filter(type = ethnicity)
        print(ethnicity)
        person = Person.objects.get(username=user_name, password=password)
        
        if email != '':
            person.email = email
        if phone_number != '':
            person.phone = phone_number
        if city != '':
            person.city = city
        if state != '':
            person.state = state
        if facebook != '':
            person.facebook = facebook
        if linkedin != '':
            person.linkedin = linkedin
        if twitter != '':
            person.twitter = twitter
        if aboutMe != '':
            person.aboutMe = aboutMe
        if jobExperience != '':
            person.jobExperience = jobExperience
        if ethnicity != '':
            person.minorityTypeID_id = ethnicityID.minorityTypeID



        person.save()

    return render(request, 'login/login.html')

def loggedTemplate(request):
    request.session.pop('logged-in', default=False)
    request.session.pop('userID', default=7)
    if request.method == 'POST':
        sUser_name = request.POST.get('user_name')
        sPassword = request.POST.get('password')
        if request.session.get('logged-in', False):
            greeting = ''
            try:
                data = Person.objects.get(user_name=sUser_name, password=sPassword)
                greeting = 'Welcome Back!'
                request.session['logged-in'] = True
                request.session['userID'] = data.personID
            except:
                #data = 'No account matches. Please try again or Create a new account'
                greeting = 'Sorry! Please try again or Create a new account'
        else:
            greeting= 'User Signed Out- Please sign in'
            request.session['logged-in'] = False
    content = {
        'data': DATABASES
    }
    return render(request, 'login/logged_in.html')
