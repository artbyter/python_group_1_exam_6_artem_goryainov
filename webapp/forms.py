from django import forms
from webapp.models import Post,UserInfo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['user']