from rest_framework import serializers
from mytest.models import Album, Track

class AlbumSerializer(serializers.ModelSerializer):
    #tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'album_name', 'artist')

class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=False, read_only=True)
    class Meta:
        model = Track
        fields = ('id', 'order', 'title', 'duration', 'album')
