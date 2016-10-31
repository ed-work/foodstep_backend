from rest_framework import viewsets

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeViewset(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
