from django.shortcuts import render
from rest_framework import generics
from .models import Parent, Pet, Veterinarian, Visit
from django.views.generic import TemplateView, ListView, DetailView
from .serializers import PetSerializer, VeterinarianSerializer, ParentSerializer, VisitSerializer
# Create your views here.

class PetList(generics.ListCreateAPIView):
  serializer_class = PetSerializer
  queryset = Pet.objects.all()

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PetSerializer
  queryset = Pet.objects.all()

class VisitList(generics.ListCreateAPIView):
  serializer_class = VisitSerializer
  queryset = Visit.objects.all()

class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()

class VeterinarianList(generics.ListCreateAPIView):
    serializer_class = VeterinarianSerializer
    queryset = Veterinarian.objects.all()

class VeterinarianDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = VeterinarianSerializer
  queryset = Veterinarian.objects.all()

class ParentList(generics.ListCreateAPIView):
  serializer_class = ParentSerializer
  queryset = Parent.objects.all()

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ParentSerializer
  queryset = Parent.objects.all()