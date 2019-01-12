from django.shortcuts import render, reverse, redirect
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from webapp.models import Post, UserInfo, User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webapp.forms import PostForm


# Create your views here.


class HandlePermissionCheck():
    def test_func(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('webauth:login')
        return redirect('webapp:post_detail', pk=self.get_object().pk)


class PostListView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        return super().get_queryset().order_by('publish_date').reverse()


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['if_own_post'] = self.request.user == self.get_object().author
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostEditView(LoginRequiredMixin, HandlePermissionCheck, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})




class PostDeleteView(LoginRequiredMixin, HandlePermissionCheck,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'

class UserListView(ListView):
    model = User
    template_name = 'users.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
