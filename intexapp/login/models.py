from django.db import models
from django.db.models.aggregates import Min, Max
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.deletion import SET_NULL

class PersonType(models.Model):
    personTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return (self.type)

class MinorityType(models.Model):
    minorityTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return (self.type)
    
class Resumes(models.Model):
    resumeID = models.AutoField(primary_key=True)
    resumefile = models.FileField(upload_to='photos/')
    uploadDate = models.DateTimeField(auto_now_add=True)

class Person(models.Model):
    personID = models.AutoField(primary_key=True)
    personTypeID = models.ForeignKey(PersonType, on_delete=models.CASCADE, default=1)
    minorityTypeID = models.ForeignKey(MinorityType, on_delete=models.CASCADE, null=True)
    resumeID = models.ForeignKey(Resumes, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)
    DOB = models.DateField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    ZIP = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    facebook = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    profilePic = models.FileField(upload_to='photos', null=True)
    aboutMe = models.CharField(max_length=250, null=True)
    jobExperience = models.CharField(max_length=250, null=True)

    @property
    def full_name(self):
        return '%s %s' % (self.firstName, self.lastName)

    def __str__(self):
        return (self.full_name)

class CategoryType (models.Model):
    categoryTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30)

    def __str__(self):
        return (self.type)
    
class CompanySize (models.Model):
    companySizeID = models.AutoField(primary_key=True)
    size = models.CharField(max_length=30)

    def __str__(self):
        return (self.size)

class Company (models.Model):
    companyID = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=70)
    categoryTypeID = models.ForeignKey(CategoryType, on_delete=models.CASCADE, null=True)
    companySizeID = models.ForeignKey(CompanySize, on_delete=models.CASCADE, null=True)
    companyDescription = models.CharField(max_length=500, null=True)
    website = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    profilePic = models.FileField(upload_to='photos', null=True)

    def __str__(self):
        return (self.companyName)

class CompanyEmployee(models.Model):
    employeeID = models.AutoField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    personID = models.ForeignKey(Person, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=20, default='Recruiter')

class JobListings(models.Model):
    jobListingID = models.AutoField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    employeeID = models.ForeignKey(CompanyEmployee, on_delete=models.CASCADE)
    categoryTypeID = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=70, default=SET_NULL)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    ZIP = models.IntegerField()
    jobDescription = models.CharField(max_length=6000)
    status = models.CharField(max_length=50, null=True)
    dateFilled = models.DateField(null=True)
    savedJobListings = models.ManyToManyField(Person, related_name='user_saved_jobs', through='SavedJobs')
    applicationsTable = models.ManyToManyField(Person, related_name='user_job_applications', through='Applications')
    
    def __str__(self):
        return (self.jobTitle)

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
    applicantResponse = models.CharField(max_length=50, null=True)

class Skills(models.Model):
    skillID = models.AutoField(primary_key=True)
    skillName = models.CharField(max_length=50)

class SkillLevel(models.Model):
    skillLevelID = models.AutoField(primary_key=True)
    skillID = models.ForeignKey(Skills, on_delete=models.CASCADE)
    level = models.IntegerField()
    jobListingID = models.ForeignKey(JobListings, on_delete=models.CASCADE)
    applicationID = models.ForeignKey(Applications, on_delete=models.CASCADE, null=True)

