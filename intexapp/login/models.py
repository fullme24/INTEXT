from django.db import models
from django.db.models.aggregates import Min

class PersonType(models.Model):
    personTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)

class MinorityType(models.Model):
    minorityTypeID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)

class Resumes(models.Model):
    resumeID = models.AutoField(primary_key=True)
    resumefile = models.ImageField(upload_to='photos')
    uploadDate = models.DateTimeField(auto_now_add=True)

class People(models.Model):
    personID = models.AutoField(primary_key=True)
    personTypeID = models.ForeignKey(PersonType, on_delete=models.CASCADE)
    minorityTypeID = models.ForeignKey(MinorityType, on_delete=models.CASCADE)
    resumeID = models.ForeignKey(Resumes, on_delete=models.CASCADE)
      

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.lasst_name)

    def __str__(self):
        return (self.full_name)