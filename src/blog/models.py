from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=240)
    body = models.TextField(blank=False,null=False)
    summary = models.TextField(default='Summary Here')
    foundHelpful = models.IntegerField(default=0)
    category = models.TextField(blank=True)
    published = models.DateField(editable=True)