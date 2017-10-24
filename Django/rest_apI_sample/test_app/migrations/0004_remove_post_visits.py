# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20171024_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='visits',
        ),
    ]
