from django.urls import path, include
from . import views
from rest_framework import routers

# endpoint name
router = routers.DefaultRouter()
router.register('albums', views.AlbumView)

urlpatterns = [
    path('', include(router.urls))
]