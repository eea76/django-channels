# Generated by Django 3.0.5 on 2020-04-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0002_sentence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='sentence',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]