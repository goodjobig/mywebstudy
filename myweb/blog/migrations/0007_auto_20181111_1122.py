# Generated by Django 2.1.3 on 2018-11-11 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181111_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='discuss',
            new_name='comments',
        ),
    ]
