from django.db import models

from django.db import models
#from rest_framework.authtoken.admin import User


class Cuisine(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()


    def __str__(self):
        return self.name





class Recipes(models.Model):
    Recipe_name = models.CharField(max_length=20)
    Ingredients= models.TextField()
    Amount=models.DecimalField(max_digits=10,decimal_places=2)
    cuisines=models.ForeignKey(Cuisine,on_delete=models.CASCADE)
    def __str__(self):
      return self.Recipe_name



