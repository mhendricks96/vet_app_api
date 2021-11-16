from rest_framework import serializers
from .models import Parent, Pet, Veterinarian, Visit

class PetSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'parent', 'animal_type', 'description', 'medications', 'primary_veterinarian')
    model = Pet

class ParentSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id','first_name', 'last_name', 'phone', 'email')
    model = Parent

class VeterinarianSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id','first_name','last_name','work_phone','home_phone','specialty')
    model = Veterinarian

class VisitSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'date', 'pet', 'vet_seen', 'reason_for_visit', 'medication_prescribed')
    model = Visit