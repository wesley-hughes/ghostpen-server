from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    ghostuser = models.ForeignKey('GhostUser', on_delete=models.CASCADE, related_name='contacts')
