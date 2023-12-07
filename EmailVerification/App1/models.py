from django.db import models


class Employee(models.Model):
    
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    organisation = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


    def __str__(self):
        return self.first_name