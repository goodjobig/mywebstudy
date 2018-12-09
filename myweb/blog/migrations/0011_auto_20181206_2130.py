# Generated by Django 2.1.3 on 2018-12-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181127_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=60, verbose_name='博客类型')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.AddField(
            model_name='blogtype',
            name='blog',
            field=models.ManyToManyField(to='blog.Blog'),
        ),
    ]