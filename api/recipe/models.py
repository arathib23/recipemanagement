
from django.db import models
from rest_framework.authtoken.admin import User


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






class Review(models.Model):
    Recipes = models.ForeignKey(Recipes, related_name='rating',
                                on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, null=True, blank=True)
    review=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Recipes']

    def __str__(self):

        rating_list = {
            '5': self.rating,
        }
        return str(max(rating_list, key=rating_list.get))
