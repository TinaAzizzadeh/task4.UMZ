from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=50)
  email = models.CharField(max_length=100)
  summary=models.CharField(max_length=300)
  skills=models.CharField(max_length=200)
  experience=models.CharField(max_length=300)
  education=models.CharField(max_length=50)
  def __str__(self):
   return f"{self.firstname}"
