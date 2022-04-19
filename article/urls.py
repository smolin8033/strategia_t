from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleWithCommentsDetailView,
    CommentCreateView,
    CommentWithCommentsDetailView
)

urlpatterns = [
    path('articles/', ArticleCreateView.as_view()),
    path('articles/<int:pk>/', ArticleWithCommentsDetailView.as_view()),
    path('comments/', CommentCreateView.as_view()),
    path('comments/<int:pk>/', CommentWithCommentsDetailView.as_view()),
]
