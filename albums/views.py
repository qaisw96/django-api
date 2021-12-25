from django.shortcuts import render
from rest_framework import viewsets
from .models import Album
from .serializers import AlbumSerializer

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer