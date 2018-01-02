# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171230_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manageuser',
            options={'verbose_name': '\u7528\u6237\u7ba1\u7406', 'verbose_name_plural': '\u7528\u6237\u7ba1\u7406', 'permissions': (('view_task', 'Can see available tasks'),)},
        ),
    ]
