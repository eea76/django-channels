# Generated by Django 3.0.5 on 2020-04-22 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0007_usersentence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersentence',
            name='sentence',
        ),
    ]