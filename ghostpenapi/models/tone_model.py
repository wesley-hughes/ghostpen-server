from django.db import models

class Tone(models.Model):
    label= models.CharField(max_length=50)