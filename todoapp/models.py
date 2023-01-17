from django.db import models

# Create your models here.
class ToDos(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    due_date = models.IntegerField()
