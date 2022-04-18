from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'content')


class CommentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'article', 'parent')


class CommentSerializer(serializers.ModelSerializer):
    comments_to_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'level', 'content', 'article', 'parent', 'comments_to_comment')

    def get_comments_to_comment(self, obj):
        return CommentSerializer(obj.get_children().filter(level__lte=3), many=True).data


class CommentWithCommentsSerializer(serializers.ModelSerializer):
    comments_to_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'level', 'content', 'article', 'parent', 'comments_to_comment')

    def get_comments_to_comment(self, obj):
        return CommentWithCommentsSerializer(obj.get_children(), many=True).data


class ArticleWithCommentsSerializer(serializers.ModelSerializer):
    comments_to_article = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'content', 'comments_to_article')

    def get_comments_to_article(self, obj):
        return CommentSerializer(obj.get_first_lvl_comments(), many=True).data
