# Generated by Django 2.1.3 on 2018-11-11 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0007_auto_20181111_1122'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('photo', models.ImageField(default='userImage/default_photo.jpg', upload_to='userImage/')),
                ('number', models.CharField(max_length=11)),
                ('collect', models.ManyToManyField(blank=True, to='blog.Blog')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户信息',
            },
        ),
    ]
