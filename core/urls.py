from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register('gifs', views.Gifs)

urlpatterns = [
    path('', include(router.urls)),
]