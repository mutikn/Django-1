# Generated by Django 2.2.5 on 2019-09-08 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190908_2249'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='item',
            name='news_item_points_d03885_idx',
        ),
    ]
