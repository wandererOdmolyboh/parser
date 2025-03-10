from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_instagram_posts


class InstagramScraperView(APIView):
    def get(self, request):
        username = request.query_params.get("username", "nasa")
        hashtag = request.query_params.get("hashtag", None)

        posts = get_instagram_posts(username, hashtag)
        return Response({"username": username, "posts": posts})
