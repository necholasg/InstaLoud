# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160127_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='album_art',
            field=models.URLField(default='http://www.shutterstock.com/music/static/1.0.37/implementation/images/album_artwork_placeholder_detail.jpg', max_length=355),
            preserve_default=False,
        ),
    ]
