from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Article, Comment
from .serializers import (
    ArticleSerializer,
    ArticleWithCommentsSerializer,
    CommentAddSerializer,
    CommentWithCommentsSerializer
)


class ArticleCreateView(CreateAPIView):
    """
    Add posts as an instance
    which we attach 1-lvl comments to
    """
    serializer_class = ArticleSerializer


class CommentCreateView(CreateAPIView):
    """
    Add comment as an instance
    which we attach either articles
    or other comments to
    """
    serializer_class = CommentAddSerializer

    def perform_create(self, serializer):
        """
        Autofill lvl-attribute of Comment model
        """
        created_comment = serializer.save()
        if created_comment.parent is None:
            created_comment.level = 1
        else:
            created_comment.level = created_comment.parent.level + 1
        created_comment.save()
        return created_comment


class ArticleWithCommentsDetailView(RetrieveAPIView):
    """
    Get the posts and all comments/nested comments to it
    until the 3 lvl
    """
    queryset = Article.objects.all()
    serializer_class = ArticleWithCommentsSerializer


class CommentWithCommentsDetailView(RetrieveAPIView):
    """
    Get the comment of a certain lvl (i.e. 3 lvl)
    and all comments/nested comments to it
    """
    queryset = Comment.objects.all()
    serializer_class = CommentWithCommentsSerializer
