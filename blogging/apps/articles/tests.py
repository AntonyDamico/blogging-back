import datetime
from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Article


def create_article(title: str, body: str,  author: User, days: int = 0) -> Article:
    created_at = timezone.now() - datetime.timedelta(days=days)
    return Article.objects.create(title=title, body=body, author=author, created_at=created_at)


def create_author() -> User:
    author = User.objects.create(username="test_user", password="pass")
    return author


class ArticleModelTest(TestCase):

    def setUp(self) -> None
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

