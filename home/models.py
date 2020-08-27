from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    login = models.TextField()
    blog = models.TextField()
    portfolio = models.TextField()
    github = models.TextField()
    linkedin = models.TextField()
