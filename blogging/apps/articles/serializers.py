from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SlugField(required=False, read_only=True)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)

    class Meta:
        model = Article
        fields = ['url', 'slug', 'title', 'body', 'image', 'author', 'createdAt']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
