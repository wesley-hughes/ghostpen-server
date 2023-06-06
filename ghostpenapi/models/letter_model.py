from django.db import models
from django.contrib.auth.models import User

class Letter(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name= 'letters')
    letter_body = models.CharField()
    date = models.DateField()

