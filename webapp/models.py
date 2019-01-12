from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_info', verbose_name='Пользователь')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    avatar = models.ImageField(verbose_name='Фотография', null=True, blank=True)
    friends = models.ManyToManyField(User, blank=True)

    @property
    def image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url


class Post(models.Model):
    title = models.CharField(max_length=254, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title
