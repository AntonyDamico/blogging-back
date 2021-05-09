from rest_framework import serializers
from .models import Article


class BaseArticleSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(required=False, read_only=True)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True, format="%Y-%m-%d %H:%M")
    author = serializers.CharField(read_only=True)
    image = serializers.ImageField(required=False)
    abstract = True

    class Meta:
        model = Article
        fields = ['url', 'slug', 'title', 'body', 'image', 'author', 'createdAt']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ArticleDetailSerializer(BaseArticleSerializer):
    pass


class ArticleListSerializer(BaseArticleSerializer):
    class Meta(BaseArticleSerializer.Meta):
        fields = ['url', 'slug', 'title', 'summary', 'image', 'author', 'createdAt']
