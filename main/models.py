from django.db import models

class Cars(models.Model):
    mod = models.CharField(max_length = 300)
    cena = models.IntegerField()
    nomer = models.CharField(max_length= 6)