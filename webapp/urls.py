from django.urls import path
from webapp.views import NewsListView, PostDetailView, UserListView, UserDetailView

app_name = 'webapp'

urlpatterns = [
    path('', NewsListView.as_view(), name='posts_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
]
