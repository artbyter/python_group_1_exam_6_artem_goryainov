from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from webapp.models import Post, UserInfo,User


# Create your views here.

class NewsListView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'users.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'