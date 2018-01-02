# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180102_1401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machistoy',
            options={'verbose_name': '\u501f\u51fa\u4fe1\u606f', 'verbose_name_plural': '\u501f\u51fa\u4fe1\u606f', 'permissions': (('view_feedback', 'view_feedback'),)},
        ),
        migrations.AlterModelOptions(
            name='manageuser',
            options={'verbose_name': '\u7528\u6237\u7ba1\u7406', 'verbose_name_plural': '\u7528\u6237\u7ba1\u7406'},
        ),
    ]
