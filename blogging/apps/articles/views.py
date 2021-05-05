from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer
