from rest_framework import serializers
from ApiCRUDapp.models import PostModel



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['author', 'title', 'description']

