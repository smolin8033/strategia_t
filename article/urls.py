from django.urls import path
from .views import ArticleCreateView, CommentCreateView

urlpatterns = [
    path('article/add/', ArticleCreateView.as_view()),
    path('comment/add/', CommentCreateView.as_view()),
]
