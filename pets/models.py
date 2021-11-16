from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

## Possibly add absolute URls

class Veterinarian(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  specialty = models.CharField(max_length=64)
  work_phone = PhoneNumberField(null=True, blank=True)
  home_phone = PhoneNumberField(null=True, blank=True)

  def __str__(self):
    return self.last_name

class Parent(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  phone = PhoneNumberField(unique = True, null = False, blank = False)
  email = models.CharField(unique = True, max_length=64)

  def __str__(self):
    return f"{self.last_name}, {self.first_name}"

class Pet(models.Model):
  name = models.CharField(max_length=64)
  primary_veterinarian = models.ForeignKey(Veterinarian, null=True, on_delete=models.SET_NULL)
  parent = models.ForeignKey(Parent, on_delete=models.PROTECT)
  animal_type = models.CharField(max_length=64)
  description = models.TextField(max_length=300)
  medications = models.TextField(max_length=400)

  def __str__(self):
    return self.name

class Visit(models.Model):
  date = models.DateField(auto_now_add=True)
  pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
  vet_seen = models.ForeignKey(Veterinarian, on_delete=models.RESTRICT)
  reason_for_visit = models.TextField(max_length=400)
  medication_prescribed = models.TextField(max_length=400)

  def __str__(self):
    return self.date
