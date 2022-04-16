from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Article
from .serializers import (
    ArticleSerializer,
    CommentSerializer,
    ArticleWithCommentsSerializer,
)


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


class ArticleWithCommentsDetailView(RetrieveAPIView):
    """
    Add comment as an instance
    which we attach either articles
    or other comments to
    """
    queryset = Article.objects.all()
    serializer_class = ArticleWithCommentsSerializer
