from django.db import models

class People(models.Model):
    user_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    lasst_name = models.CharField(max_length=50, blank=True, null=True)  
    city = models.CharField(max_length=50, blank=True, null=True)  
    state = models.CharField(max_length=50, blank=True, null=True)  
    zip = models.CharField(max_length=50, blank=True, null=True)  

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.lasst_name)

    def __str__(self):
        return (self.full_name)