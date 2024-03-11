from rest_framework import serializers
from django.contrib.auth.models import User
from recipe.models import Recipes,Cuisine,Review


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ('id','name', 'desc')

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id','Recipe_name', 'Ingredients','Amount','cuisines')

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=('id','username','password')

    def create(self, validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=('Recipes','rating','review','created','updated')