from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'content')


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'article', 'parent')


class CommentSerializer(serializers.ModelSerializer):
    comments_to_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'article', 'parent', 'comments_to_comment')

    def get_comments_to_comment(self, obj):
        return CommentSerializer(obj.children(), many=True).data


class ArticleWithCommentsSerializer(serializers.ModelSerializer):
    comments_to_article = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'content', 'comments_to_article')

    def get_comments_to_article(self, obj):
        return CommentSerializer(obj.get_1_lvl_comments(), many=True).data
