from django.conf import settings
from django.core.cache import cache

from apps.blog.models import Post


def get_posts_cache():
    if settings.CACHE_ENABLED:
        key = 'posts_list'
        posts_list = cache.get(key)
        if posts_list is None:
            posts_list = Post.objects.filter(is_published=True)
            cache.set(key, posts_list)
    else:
        posts_list = Post.objects.filter(is_published=True)
    return posts_list
