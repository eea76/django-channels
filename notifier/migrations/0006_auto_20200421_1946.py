# Generated by Django 3.0.5 on 2020-04-21 19:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifier', '0005_sentence_is_real'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='already_played',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='was_guessed_correctly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sentence',
            name='guessed_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='sentence_guessed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sentence',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sentence',
            name='vote_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
