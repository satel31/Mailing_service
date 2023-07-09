from django.urls import path
from django.views.decorators.cache import cache_page

from apps.blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    # blog urls
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/<int:pk>', cache_page(60)(PostDetailView.as_view()), name='post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
