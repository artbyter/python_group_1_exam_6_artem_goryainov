from django.urls import path
from webauth.views import UserLoginView
from django.contrib.auth.views import LogoutView

app_name = 'webauth'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
]
