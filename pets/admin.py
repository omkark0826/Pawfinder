from django.contrib import admin
from .models import Animal, Shelter, AnimalPhoto

class AnimalPhotoInline(admin.TabularInline):
    model = AnimalPhoto
    extra = 5
    max_num = 5

class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalPhotoInline]

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Shelter)

# Register your models here.
