from django.shortcuts import render, reverse, redirect
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from webapp.models import Post, UserInfo, User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webapp.forms import PostForm, UserForm


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


class PostDeleteView(LoginRequiredMixin, HandlePermissionCheck, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'


class UserListView(ListView):
    model = UserInfo
    template_name = 'users.html'


class UserDetailView(DetailView):
    model = UserInfo
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object.user.pk).order_by('publish_date').reverse()
        context['is_own_profile'] = self.request.user.pk == self.get_object().user.pk
        return context


# class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = User
#     template_name = 'user_edit.html'
#     form_class = UserForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_own_profile'] = self.request.user.pk == self.get_object().pk
#         print(self.request.user.pk)
#         print(self.get_object().pk)
#
#         context['user_name'] = self.request.user.username
#         return context
#
#     def get_initial(self):
#         initial = super(UserEditView, self).get_initial()
#         initial['phone'] = self.get_object().user_info.phone
#
#         initial['friends'] = self.get_object().user_info.friends.all()
#         return initial
#
#     def test_func(self):
#
#         return self.request.user.pk == self.get_object().pk
#
#     def handle_no_permission(self):
#         if not self.request.user.is_authenticated:
#             return redirect('webauth:login')
#         return redirect('webapp:user_detail', pk=self.get_object().pk)
#
#     def get_success_url(self):
#         return reverse('webapp:user_detail', kwargs={'pk': self.object.pk})
#
#     def form_valid(self, form):
#         self.get_object().user_info.phone = form.fields['phone'].label
#         return super().form_valid(form)


class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserInfo
    template_name = 'user_edit.html'
    form_class = UserForm



    def test_func(self):
        print(self.request.user.pk)
        print(self.get_object())
        return self.request.user.user_info == self.get_object()

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('webauth:login')
        return redirect('webapp:user_detail', pk=self.object.pk)

    def get_success_url(self):
         return reverse('webapp:user_detail', kwargs={'pk': self.object.pk})