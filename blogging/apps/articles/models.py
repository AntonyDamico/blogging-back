from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Article(models.Model):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    author = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            random_string = get_random_string(length=10)
            slug_string = f'{self.title} {random_string}'
            self.slug = slugify(slug_string)

        super(Article, self).save(*args, **kwargs)

    @property
    def summary(self) -> str:
        # gets only the 30 first characters of the body
        return self.body[:20] + '...'

    def __str__(self):
        return self.title
