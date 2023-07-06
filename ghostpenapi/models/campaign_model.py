from django.db import models

class Campaign(models.Model):
    label= models.CharField(max_length=50)
    description= models.CharField(max_length=1500, null=True)
    contacts = models.ManyToManyField('Contact', related_name='campaigns')
    ghostuser = models.ForeignKey('GhostUser', on_delete=models.CASCADE, related_name='campaigns')
2