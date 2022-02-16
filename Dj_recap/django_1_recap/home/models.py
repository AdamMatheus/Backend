from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name