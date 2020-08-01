from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from core.models import Gif
from core.serializers import GifsSerializer

# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class Gifs(viewsets.ModelViewSet):
    serializer_class = GifsSerializer
    pagination_class = CustomPagination
    queryset = Gif.objects.all()