
from rest_framework import serializers
from watchlist_app.models import StreamPlatform


class streamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = StreamPlatform
        fields = "__all__"
        