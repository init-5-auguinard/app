from django.db import models

# Create your models here.

class Newsletter(models.Model):
    nom   = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email