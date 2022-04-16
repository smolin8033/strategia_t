from django.db import models


class Article(models.Model):
    content = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.content)

    def get_1_lvl_comments(self):
        return Comment.objects.filter(article=self, parent=None)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    parent = models.ForeignKey('self', related_name='replies', blank=True, null=True, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)

    def __str__(self):
        return str(self.content)

    def children(self):
        return Comment.objects.filter(parent=self)
