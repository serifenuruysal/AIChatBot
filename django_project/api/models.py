from django.db import models

# Create your models here.

class UserMessage(models.Model):
    user_input = models.TextField()
    response = models.TextField()
