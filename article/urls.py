from django.urls import path
from .views import (
    ArticleCreateView,
    CommentCreateView,
    ArticleWithCommentsDetailView,
)

urlpatterns = [
    path('article/', ArticleCreateView.as_view()),
    path('comment/', CommentCreateView.as_view()),
    path('article/<int:pk>/', ArticleWithCommentsDetailView.as_view()),
]
