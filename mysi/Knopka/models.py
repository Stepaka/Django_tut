from django.db import models

class opa(models.Model):
    name=models.CharField(max_length=100)
    text=models.TextField()
    date=models.DateTimeField()

def Tname(self):
    return self.name
