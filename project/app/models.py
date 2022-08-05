from django.db import models

# Create your models here.
class Repository(models.Model):
    docid = models.CharField(max_length=10)
    docname = models.CharField(max_length=70)
    docloc = models.CharField(max_length=100)
    tags = models.CharField(max_length=70)