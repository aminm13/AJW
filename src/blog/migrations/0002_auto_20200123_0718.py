# Generated by Django 3.0.2 on 2020-01-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='foundHelpful',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default='Summary Here'),
        ),
    ]
