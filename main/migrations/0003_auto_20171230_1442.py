# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171230_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageuser',
            name='keshi_f',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xa7\x91\xe5\xae\xa4', blank=True, to='main.keshi', null=True),
        ),
    ]
