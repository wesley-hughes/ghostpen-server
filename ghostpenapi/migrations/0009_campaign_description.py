# Generated by Django 4.2.2 on 2023-07-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpenapi', '0008_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='description',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]
