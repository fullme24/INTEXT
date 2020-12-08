from django.contrib import admin
from .models import Person, PersonType, MinorityType, Resumes, Company, CompanyEmployee, CompanySize, CategoryType, JobListings, JobOffers, SavedJobs, Applications, SkillLevel, Skills

admin.site.register(Person)
admin.site.register(PersonType)
admin.site.register(MinorityType)
admin.site.register(Resumes)
admin.site.register(Company)
admin.site.register(CompanyEmployee)
admin.site.register(CompanySize)
admin.site.register(CategoryType)
admin.site.register(JobListings)
admin.site.register(JobOffers)
admin.site.register(SavedJobs)
admin.site.register(SkillLevel)
admin.site.register(Skills)
admin.site.register(Applications)
