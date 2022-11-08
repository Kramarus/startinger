from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=30)
    comment = models.CharField(max_length=600)
    def __str__(self):
        return f"{self.first_name} {self.last_name} from {self.location}. Email: {self.email}.  Comment: {self.comment}"
    
    def get_absolute_url(self):
        return "/"

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=30)
    message = models.CharField(max_length=600)
    def __str__(self):
        return f"{self.name} from {self.location}. Message: {self.message}"
    
    def get_absolute_url(self):
        return "/"

class Newsletter(models.Model):
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.email
        
    def get_absolute_url(self):
        return "/"
