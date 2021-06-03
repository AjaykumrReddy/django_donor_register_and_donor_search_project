from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


BloodGroups = (
    ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),)
Gender = (('M', 'Male'), ('F', 'Female'))


class Donor(models.Model):
    name = models.CharField(max_length=120)
    gender = models.CharField(max_length=100, choices=Gender, null=True)
    Age = models.IntegerField()
    Blood_Group = models.CharField(max_length=100, choices=BloodGroups)
    phone = models.BigIntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
