from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserCreation(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=18)
    
    def create(self):
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        user.save()
        return user.id
  # Return the generated user ID

    def __str__(self):
        return self.username
