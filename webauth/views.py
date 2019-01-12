from django.shortcuts import render,reverse
from django.contrib.auth.views import LoginView
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('webapp:user_detail', args=[self.request.user.pk])