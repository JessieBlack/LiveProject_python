from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'cities'
class Zip(models.Model):
    name = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name

# Create your models here.
