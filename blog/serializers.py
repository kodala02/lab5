from rest_framework import serializers
from blog import models


class PostSerialisers(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("posted_by_id", "message")
