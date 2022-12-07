from django.db import models


# Create your models here.
class Inspections(models.Model):
    date = models.DateField()
    patient_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=250)
    diagnosis = models.CharField(max_length=500)
    appointment = models.CharField(max_length=500)
    doctor = models.CharField(max_length=50)


class db_medicines(models.Model):
    name = models.CharField(max_length=50)
    instructions = models.CharField(max_length=1000)
    intended_action = models.CharField(max_length=500)
    side_effects = models.CharField(max_length=500)
    disease = models.CharField(max_length=100)


class Doctors(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)

