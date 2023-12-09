from rest_framework.views import APIView
from rest_framework.response import Response

from blog import models
from .serializers import PostSerialisers


class PublicPostList(APIView):
    """

    return the most recent public posts by all users
    """

    def get(self, request):
        msgs = models.Post.objects.public_posts()[:5]
        data = PostSerialisers(msgs, many=True).data
        return Response(data)
