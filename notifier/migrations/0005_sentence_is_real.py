# Generated by Django 3.0.5 on 2020-04-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0004_auto_20200421_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='is_real',
            field=models.BooleanField(default=False),
        ),
    ]