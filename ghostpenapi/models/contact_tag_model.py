from django.db import models
from django.contrib.auth.models import User

class ContactTag(models.Model):
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)