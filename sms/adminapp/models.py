from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.contrib.auth.models import User
class studentList(models.Model):
    Register_Number=models.CharField(max_length=20,unique=True)
    Name=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Register_Number



##FEEDBACK FORM ##############
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Add this field
    comment = models.TextField(max_length=160)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email}), Phone: {self.phone_number}"

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number} - {self.address}"


