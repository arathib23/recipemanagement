"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from recipe import views

app_name="recipe"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cuisines/',views.Cuisinelist.as_view()),
    path('cuisine/<int:pk>',views.Cuisinedetails.as_view()),
    path('recipes/<int:pk>/', views.RecipeRetrieveView.as_view(), name='recipe-retrieve'),
    path('recipes/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-destroy'),
    path('Recipes/',views.Recipeslist.as_view()),
    path('Recipe/<int:pk>',views.Recipesdetails.as_view()),
    path('logout',views.user_logout.as_view()),
    path('review',views.Userreview.as_view()),
]
