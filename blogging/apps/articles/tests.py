from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Article


class ArticleModelTest(TestCase):

    def test_adding_slug_to_article(self):
        """El artículo creado debe tenner un slug"""
        author = User(username="test_user", password="pass")
        author.save()

        title = 'This is the article title'
        article = Article(title=title, author=author)
        article.save()

        title_slug = slugify(title)
        self.assertNotEqual(article.slug, '')
        self.assert_(article.slug.startswith(title_slug))

