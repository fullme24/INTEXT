from django.shortcuts import render
# from intexapp.login.models import Person


# Create your views here.
def ProfileTemplate(request) :
        # data = Person.objects.all()
    
        # context = {
        #     "our_emps" : data
        # }
        return render(request, 'profile_info/myprofile.html')



def CompanyProfileTemplate(request) :
    return render(request, 'profile_info/companyprofile.html')

def RecruiterProfileTemplate(request) :
    return render(request, 'profile_info/recruiterprofile.html')