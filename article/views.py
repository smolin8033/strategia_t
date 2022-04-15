from rest_framework.generics import CreateAPIView
from .serializers import ArticleSerializer, CommentSerializer


class ArticleCreateView(CreateAPIView):
    """
    Add article as an instance
    which we attach 1-lvl comments to
    """
    serializer_class = ArticleSerializer


class CommentCreateView(CreateAPIView):
    """
    Add comment as an instance
    which we attach either articles
    or other comments to
    """
    serializer_class = CommentSerializer
