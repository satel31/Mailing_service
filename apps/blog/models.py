from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}

class Post(models.Model):
    post_title = models.CharField(max_length=250, verbose_name='Post Title')
    text = models.TextField(verbose_name='Text', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='Preview', **NULLABLE)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    views = models.IntegerField(default=0, verbose_name='Views')

    def delete(self, *args, **kwargs):
        if self.is_published:
            self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.post_title}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

