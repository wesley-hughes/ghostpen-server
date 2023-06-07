from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    tags = models.ManyToManyField('Tag', through = 'ContactTag', related_name= "contacts")
    ghostuser = models.ForeignKey('GhostUser', on_delete=models.CASCADE, related_name='user_contacts')

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"