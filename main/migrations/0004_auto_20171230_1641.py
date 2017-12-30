# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171230_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machistoy',
            name='beizhu',
            field=models.CharField(max_length=255, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
