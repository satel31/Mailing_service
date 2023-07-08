from django.urls import path

from apps.blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    # blog urls
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
