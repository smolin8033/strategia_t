# Generated by Django 4.0.4 on 2022-04-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comment_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='author', max_length=70),
            preserve_default=False,
        ),
    ]
