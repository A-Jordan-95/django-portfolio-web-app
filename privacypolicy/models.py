from django.db import models

# Create your models here.
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

