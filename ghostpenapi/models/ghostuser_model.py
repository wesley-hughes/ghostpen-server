from django.db import models
from django.contrib.auth.models import User

class GhostUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)

    @property
    def first_name(self):
        return f'{self.user.first_name}'
    def last_name(self):
        return f'{self.user.last_name}'