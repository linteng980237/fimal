from django.db import models

class Dog(models.Model):
    kind = models.CharField(max_length=128, unique=True)
    tall = models.CharField(max_length=128)
    kg = models.CharField(max_length=128)
    guts = models.CharField(max_length=128)
    live = models.CharField(max_length=128)
    habit = models.TextField()
    history = models.TextField()
    
    def __str__(self):
        return self.kind