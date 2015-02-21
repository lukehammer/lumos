# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trick',
            name='length',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
