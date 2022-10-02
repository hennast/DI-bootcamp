from django.db import models

# Create your models here.
class workout(models.Model):
    Exercise_name = models.CharField(max_length=50)
    Exercise_type = models.CharField(max_length=40)
    Exercise_difficulty = models.FloatField()
    