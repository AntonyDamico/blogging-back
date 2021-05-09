import datetime
import json
from django.urls import reverse
from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import RequestsClient
from .models import Article


def create_article(title: str, body: str, author: User, days: int = 0) -> Article:
    created_at = timezone.now() - datetime.timedelta(days=days)
    return Article.objects.create(title=title, body=body, author=author, created_at=created_at)


def create_author() -> User:
    author = User.objects.create(username="test_user", password="pass")
    return author


class ArticleModelTest(TestCase):

    def setUp(self) -> None:
        title = 'This is the article title'
        body = 'This is the body of the article, it has more than 20 chars'
        author = create_author()
        self.article = create_article(title, body, author)

    def test_adding_slug_to_article(self) -> None:
        """El artículo creado debe tenner un slug"""
        title_slug = slugify(self.article.title)
        self.assertNotEqual(self.article.slug, '')
        self.assert_(self.article.slug.startswith(title_slug))

    def test_summary_is_correct(self) -> None:
        """El summary del artículo debe ser los primeros 20 caracters del body con tres puntos al final"""
        summary = self.article.body[:20] + '...'
        self.assertEqual(self.article.summary, summary)


class ArticleViewSets(TestCase):

    def setUp(self) -> None:
        self.author = create_author()

    def test_get_sorted_by_title(self) -> None:
        """El endpoint debe devolver los artículos ordenados por título"""
        article1 = create_article('bbbb', '', self.author)
        article2 = create_article('cccc', '', self.author)
        article3 = create_article('aaaa', '', self.author)
        slug_list = [article.slug for article in [article3, article1, article2]]

        url = reverse('article-list') + '?sort=title'
        response = self.client.get(url)
        response_data = json.loads(response.content)
        response_slugs = [response_article['slug'] for response_article in response_data]
        print(slug_list, response_slugs)
        self.assertEqual(slug_list, response_slugs)
