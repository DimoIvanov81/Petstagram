from django.contrib import admin

from petstagram.pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    pass

