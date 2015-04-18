# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150417_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.CharField(default=b'T', max_length=15, choices=[(b'D', b'Defect'), (b'E', b'Enhancement'), (b'T', b'Task')]),
            preserve_default=True,
        ),
    ]
