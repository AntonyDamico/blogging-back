from django.db import models


class Article(models.Model):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.title
