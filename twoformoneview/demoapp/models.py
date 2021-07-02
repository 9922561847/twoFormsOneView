from django.db import models

# Create your models here.

class Contry(models.Model):
    contry = models.CharField(max_length=30)

    def __str__(self):
        return self.contry


class City(models.Model):
    contry = models.ForeignKey(Contry,on_delete = models.CASCADE)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Profile(models.Model):
    name = models.CharField(max_length=100)
    contry = models.ForeignKey(Contry,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.name 