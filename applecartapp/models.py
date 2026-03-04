from django.db import models

# Create your models here.
class Buy (models.Model):
    name = models.CharField (max_length=100)
    mobile = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    address = models.TextField(max_length=300)

    def __str__(self):
        return self.name

