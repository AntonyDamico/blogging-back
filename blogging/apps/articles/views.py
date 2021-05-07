from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleViewSet(ModelViewSet):
    model = Article
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort')
        if sort_by == 'title':
            return Article.objects.order_by('title')
        return Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
