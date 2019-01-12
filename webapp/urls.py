from django.urls import path
from webapp.views import PostListView, PostDetailView, UserListView, UserDetailView, PostCreateView, PostEditView, \
    PostDeleteView,UserEditView

app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/edit/<int:pk>', UserEditView.as_view(), name='user_edit'),
]
