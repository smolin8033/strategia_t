from django.urls import path
from .views import (
    ArticleCreateView,
    CommentCreateView,
    ArticleWithCommentsDetailView,
    CommentWithCommentsDetailView
)

urlpatterns = [
    path('article/', ArticleCreateView.as_view()),
    path('article/<int:pk>/', ArticleWithCommentsDetailView.as_view()),
    path('comment/', CommentCreateView.as_view()),
    path('comment/<int:pk>/', CommentWithCommentsDetailView.as_view()),
]
