from django.shortcuts import render
from recipe.models import Cuisine,Recipes,Review
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from recipe.serializers import CuisineSerializer,RecipesSerializer,ReviewSerializer
from recipe.serializers import UserSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import status
from rest_framework import mixins,generics,viewsets




class Cuisinelist(generics.ListCreateAPIView):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class Cuisinedetails(generics.RetrieveUpdateDestroyAPIView):
   queryset = Cuisine.objects.all()
   serializer_class = CuisineSerializer





class Recipeslist(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer



class RecipeRetrieveView(RetrieveAPIView):
    serializer_class = RecipesSerializer
    queryset = Recipes.objects.all()

class RecipeUpdateView(UpdateAPIView):
    serializer_class = RecipesSerializer
    queryset = Recipes.objects.all()


class RecipeDeleteView(DestroyAPIView):
    serializer_class = RecipesSerializer
    queryset = Recipes.objects.all()

class Recipesdetails(APIView):
    def get_object(self,request,pk):
        try:
            return Cuisine.objects.get(pk=pk)
        except:
            raise Http404
    def get(self,request,pk):
        c=self.get_object(request, pk)
        r=Recipes.objects.filter(cuisines=c)
        rec=RecipesSerializer(r,many=True)
        return Response(rec.data)


class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class user_logout(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class Userreview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

