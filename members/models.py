from django.db import models

# Create your models here.
class Welcome(models.Model):
    name= models.CharField(max_length=255)
    age=models.IntegerField()
    
    def __str__(self):
        return f"{self.name}{self.age}"