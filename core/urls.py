from django.conf.urls import url, include
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'gifs', views.Gifs)

urlpatterns = [
    url('', include(router.urls)),
]