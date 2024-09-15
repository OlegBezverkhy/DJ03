# Generated by Django 5.1.1 on 2024-09-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_post_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news_post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
