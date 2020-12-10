from django.shortcuts import render
from login.models import *
import urllib
import json
import random
from random import randint

# Create your views here.
def ProfileTemplate(request) :
    data = Person.objects.all()

    context = {
            "person" : data
    }
    return render(request, 'profile_info/myprofile.html', context)

def CompanyProfileTemplate(request) :
    return render(request, 'profile_info/companyprofile.html')

def RecruiterProfileTemplate(request) :
    return render(request, 'profile_info/recruiterprofile.html')

def employeeLookTemplate(request, personID, personTypeID):
    data = Person.objects.all()
    context = {
        'person' : data,
        'personID' : personID,
        'personTypeID' : personTypeID,
    }
    return render(request, 'profile_info/employee_look.html', context)

def get_infor_for_profile(request, personID, personTypeID):
    fullName = request.POST.get('name')

    recruiterPersonID = personID
    print(recruiterPersonID)
    recruiterPersonTypeID = personTypeID
    print(recruiterPersonTypeID)

    test = fullName.split()
    firstName = test[0]
    lastName = test[1]
    data = Person.objects.get(firstName = firstName, lastName = lastName)
    personID = data.personID
    personTypeID = data.personTypeID
    if (personTypeID == 2) :
        company_empData = CompanyEmployee.objects.get(personID_id=personID)
        empID = company_empData.employeeID
        companyData = Company.objects.get(companyID=empID)
    else:
        companyData = "Just wait and see! They will have a job yet!"

    #The Follwoing code is meant to call the recommender. The recommender works fine on it's one, however, when we tried to match the data up to our own postegress database
    #it did not function right. This was very frustrating, but we are a team of three working in two time zones so we do not have the capacity to fix it at this time

    emp = CompanyEmployee.objects.get(personID_id = recruiterPersonID)
    organizational = emp.companyID_id

    application = Applications.objects.filter(personID_id=personID)
    application = application[0]
    matching_skills = application.matchingSkills

    boomer = recommender(organizational, personID, matching_skills)

    boomerNames = []

    #for bugtestting
    names = ["John Maher", "Tracie Vargas", "Roy Byrd", "Micheal Bright", "Brian Vasquez", "Maria Smith", "Jesse Joseph", "Anne Hunter", "Fancis Branton", "Robert Lane", "Patricia Wallace", "Fernando Perez", "Jeremy Caudill"]
    
    for iCount in boomer:
        try:
            data = Person.objects.get(personID=iCount)
            data2 = data.firstName
            data2 += " "
            data2 += data.lastName
        except:
            ran = randint(0,12)
            data2 = names[ran]
            boomerNames.append(data2)

    context = {
       "person" : data,
        "company": companyData,
        "personID" : personID,
        "personTypeID" : personTypeID,
        'recruiterPersonID' : recruiterPersonID,
        'recruiterPersonTypeID' : recruiterPersonTypeID,
        'names' : boomerNames,
    }

    return render(request, 'login/myprofile.html', context)

def recommender(organizational, personID, matching_skills):
    #this is the recomender
    data =  {

            "Inputs": {

                    "input":
                    {
                        "ColumnNames": ["organization_id", "user_id", "matching_skills"],
                        "Values": [ [organizational, personID, matching_skills ] ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/6cd2963c1b214c0c956a2c7ac293beea/services/fc0ae6971b8a4f639c3638843aec56e5/execute?api-version=2.0&details=true'
    api_key = '17JKkH/v9DoXo1+CPqd4FzeZP31z7QESd1l0a2wEU8IRJWZ+BKUvgNzbR53Nck+rr3/a1Ynt/BUNRpD0HHMrjA==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result)
        boomer = result['Results']['user_id']['value']['Values'][0]
        return (boomer)
    except:
        print('Not working')