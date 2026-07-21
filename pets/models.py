from django.db import models


# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    instagram = models.CharField(max_length = 100, blank = True)
    contact_whatsapp = models.CharField(max_length=15, blank = True)
    def __str__(self):
        return self.name



class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    approx_age = models.CharField(max_length=50)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    SIZE_CHOICES = [
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    ]
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    story = models.TextField()
    photo = models.ImageField(upload_to="animals/")
    STATUS_CHOICES = [
        ("available", "Available"),
        ("pending", "Pending"),
        ("adopted", "Adopted")
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


