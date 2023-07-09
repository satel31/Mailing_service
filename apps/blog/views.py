from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from apps.blog.forms import PostForm
from apps.blog.models import Post
from apps.blog.services import get_posts_cache


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    permission_required = 'blog.add_post'
    success_url = reverse_lazy('blog:blog')


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_posts_cache()
        context_data['title'] = 'Our blog'
        return context_data


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object'].post_title
        return context_data

    def get_object(self, queryset=None):
        """Adds views +1 when the post is opened"""
        object = self.model.objects.get(pk=self.kwargs['pk'])
        if object:
            object.views += 1
            object.save()
        return object


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    permission_required = 'blog.change_post'

    def get_success_url(self):
        return reverse_lazy('blog:post', kwargs={'pk': self.kwargs['pk']})


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = 'blog.delete_post'
    success_url = reverse_lazy('blog:blog')
