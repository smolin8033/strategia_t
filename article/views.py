from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Article, Comment
from .serializers import (
    ArticleSerializer,
    ArticleWithCommentsSerializer,
    CommentSerializer,
    CommentChildSerializer,
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
    serializer_class = CommentChildSerializer

    def perform_create(self, serializer):
        created_comment = serializer.save()
        if created_comment.parent is None:
            created_comment.level = 1
        else:
            created_comment.level = created_comment.parent.level + 1
        created_comment.save()
        return created_comment


class ArticleWithCommentsDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleWithCommentsSerializer
