# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='owner',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='component',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='uid',
            new_name='ticket',
        ),
        migrations.AddField(
            model_name='task',
            name='product',
            field=models.CharField(default='--', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'U', max_length=15, choices=[(b'U', b'Unconfirmed'), (b'N', b'New'), (b'A', b'Assigned'), (b'R', b'Reopened'), (b'C', b'Closed')]),
            preserve_default=True,
        ),
    ]
