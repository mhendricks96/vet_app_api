from django.contrib import admin
from .models import Parent, Pet, Veterinarian, Visit


# Register your models here.
admin.site.register(Parent)
admin.site.register(Pet)
admin.site.register(Veterinarian)
admin.site.register(Visit)