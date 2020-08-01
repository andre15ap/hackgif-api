from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from core.models import Gif
from core.serializers import GifsSerializer

# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 5

class Gifs(viewsets.ReadOnlyModelViewSet,):
    pagination_class = CustomPagination
    serializer_class = GifsSerializer
    queryset = Gif.objects.all()