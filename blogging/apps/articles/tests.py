from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Article


class ArticleModelTest(TestCase):

    def setUp(self):
        self.set_author()
        self.set_article()

    def set_author(self):
        author = User.objects.create(username="test_user", password="pass")
        self.author = author

    def set_article(self):
        title = 'This is the article title'
        body = 'This is the body of the article, it has more than 20 chars'
        article = Article.objects.create(title=title, body=body, author=self.author)
        self.article = article

    def test_adding_slug_to_article(self):
        """El artículo creado debe tenner un slug"""
        title_slug = slugify(self.article.title)
        self.assertNotEqual(self.article.slug, '')
        self.assert_(self.article.slug.startswith(title_slug))
