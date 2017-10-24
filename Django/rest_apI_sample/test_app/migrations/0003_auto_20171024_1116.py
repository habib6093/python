# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20171024_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
    ]
