from django.db import models

class Letter(models.Model):

    ghostuser = models.ForeignKey('GhostUser', on_delete=models.CASCADE, related_name='user_letters', default=None)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name= 'letters')
    letter_body = models.CharField(max_length=5000)
    date = models.DateField()
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE, related_name= 'campaign_letters', null=True)

