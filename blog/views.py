from django.shortcuts import render
from .serializers import TagSerializer, CategorySerializer, CitySerializer
from .models import Category, City, Tag
from rest_framework import generics


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        cat = self.request.query_params.get('cat')
        title = self.request.query_params.get('title')
        if tag:
            return City.objects.filter(tags__name__icontains=tag)
        if cat:
            return City.objects.filter(category__name__icontains=cat)
        if title:
            return City.objects.filter(title__name__icontains=title)

        else:
            return City.objects.all()

