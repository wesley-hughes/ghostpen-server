from django.db import models

class Campaign(models.Model):
    label= models.CharField(max_length=50)