from django.db import models

# Create your models here.
class events(models.Model):
    name = models.CharField(max_length=100)
    club_name=models.CharField(max_length=100)
    description=models.CharField(max_length=3000)
    loc=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
class clubs(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=3000)
    def __str__(self):
        return self.name
class registration_details(models.Model):
    name = models.CharField(blank=False, max_length = 255)
    roll_no = models.CharField(blank=False, max_length = 255)
    email = models.EmailField(blank=False,max_length=255)
    phone = models.CharField(blank=False, max_length = 255)
    event = models.CharField(blank=False, max_length = 255)
class registration(models.Model):
    name = models.CharField(blank=False, max_length = 255)
    roll_no = models.CharField(blank=False, max_length = 255)
    email = models.EmailField(blank=False,max_length=255)
    phone = models.CharField(blank=False, max_length = 255)
    event = models.CharField(blank=False, max_length = 255)
  
