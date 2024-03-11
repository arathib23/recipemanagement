
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import filters


from Recipe.serializers import UserSerializer
from Recipe.serializers import CuisineSerializer,RecipesSerializer
from rest_framework.response import Response
from Recipe.models import Recipes,Cuisine
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins,generics,viewsets

@api_view(['GET','POST',])
def Cuisinelist(request):
    if(request.method=="GET"):
        Cuisines=Cuisine.objects.all()
        c=CuisineSerializer(Cuisines,many=True)
        return Response(c.data)
    elif(request.method=="POST"):
        c=CuisineSerializer(data=request.data)
        if c.is_valid():
            c.save()
            return Response(c.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Cuisinedetail(request,pk):
    try:
        Cuisines=Cuisine.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        c = CuisineSerializer(Cuisines)
        return Response(c.data)
    elif(request.method=="PUT"):
        c=CuisineSerializer(Cuisines,data=request.data)
        if(c.is_valid()):
            c.save()
            return Response(c.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=="DELETE"):
        Cuisines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST',])
def Recipelist(request):
    if(request.method=="GET"):
        Recipe=Recipes.objects.all()
        R=RecipesSerializer(Recipe,many=True)
        return Response(R.data)
    elif(request.method=="POST"):
        R=RecipesSerializer(data=request.data)
        if R.is_valid():
            R.save()
            return Response(R.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def Recipedetails(request,pk):
    try:
        Recipe=Recipes.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        R = RecipesSerializer(Recipe)
        return Response(R.data)
    elif(request.method=="PUT"):
        R=RecipesSerializer(Recipe,data=request.data)
        if(R.is_valid()):
            R.save()
            return Response(R.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=="DELETE"):
        Recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Recipessearch(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cuisines']