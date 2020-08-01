from rest_framework import serializers
from core.models import Gif

class GifsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gif
        fields = (
            'id',
            'gif_url',
            'votes',
        )