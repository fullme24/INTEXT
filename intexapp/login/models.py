from django.db import models
from django.db.models.aggregates import Min
from django.db.models.base import ModelStateFieldsCacheDescriptor

class PersonType(models.Model):
    personTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)

class MinorityType(models.Model):
    minorityTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)

class Resumes(models.Model):
    resumeID = models.AutoField(primary_key=True)
    #resumefile = models.ImageField(upload_to='photos')
    uploadDate = models.DateTimeField(auto_now_add=True)

class Person(models.Model):
    personID = models.AutoField(primary_key=True)
    personTypeID = models.ForeignKey(PersonType, on_delete=models.CASCADE)
    minorityTypeID = models.ForeignKey(MinorityType, on_delete=models.CASCADE)
    resumeID = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=14)
    DOB = models.DateField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    ZIP = models.IntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    long = models.DecimalField(max_digits=11, decimal_places=8)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    #profilePic = models.ImageField(upload_to='photos')
    aboutMe = models.CharField(max_length=250)
    jobExperience = models.CharField(max_length=250)

    @property
    def full_name(self):
        return '%s %s' % (self.firstName, self.lastName)

    def __str__(self):
        return (self.full_name)

class CategoryType (models.Model):
    categoryTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)
    
class CompanySize (models.Model):
    companySizeID = models.AutoField(primary_key=True)
    size = models.CharField(max_length=15)

class Company (models.Model):
    companyID = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=30)
    categoryTypeID = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    companySizeID = models.ForeignKey(CompanySize, on_delete=models.CASCADE)
    companyDescription = models.CharField(max_length=250)
    website = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    #profilePic = models.ImageField(upload_to='photos')

class CompanyEmployee(models.Model):
    employeeID = models.AutoField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=20)

class JobListings(models.Model):
    jobListingID = models.AutoField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    employeeID = models.ForeignKey(CompanyEmployee, on_delete=models.CASCADE)
    categoryTypeID = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    ZIP = models.IntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    long = models.DecimalField(max_digits=11, decimal_places=8)
    jobDescription = models.CharField(max_length=500)
    status = models.CharField(max_length=15)
    dateFilled = models.DateField()

class SavedJobs(models.Model):
    savedJobID = models.AutoField(primary_key=True)
    jobListingID = models.ForeignKey(JobListings, on_delete=models.CASCADE)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    dateSaved = models.DateField(auto_now=True)

class Applications(models.Model):
    applicationID = models.AutoField(primary_key=True)
    jobListingID = models.ForeignKey(JobListings, on_delete=models.CASCADE)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    resumeID = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    matchingSkills = models.IntegerField()
    dateApplied = models.DateField(auto_now=True)

class JobOffers(models.Model):
    jobOfferID = models.AutoField(primary_key=True)
    jobListingID = models.ForeignKey(JobListings, on_delete=models.CASCADE)
    applicationID = models.ForeignKey(Applications, on_delete=models.CASCADE)
    resumeID = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    startDate = models.DateField()
    applicantResponse = models.CharField(max_length=15)

class Skills(models.Model):
    skillID = models.AutoField(primary_key=True)
    skillName = models.CharField(max_length=30)

class SkillLevel(models.Model):
    skillLevelID = models.AutoField(primary_key=True)
    skillID = models.ForeignKey(Skills, on_delete=models.CASCADE)
    level = models.IntegerField()
    jobListingID = models.ForeignKey(JobListings, on_delete=models.CASCADE)
    applicationID = models.ForeignKey(Applications, on_delete=models.CASCADE)

