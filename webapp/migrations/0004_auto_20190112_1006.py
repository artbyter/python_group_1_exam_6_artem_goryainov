# Generated by Django 2.1.3 on 2019-01-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190112_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]
