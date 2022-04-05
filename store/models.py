from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.name
