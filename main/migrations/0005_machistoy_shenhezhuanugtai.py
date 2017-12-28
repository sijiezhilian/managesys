# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171228_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='machistoy',
            name='shenhezhuanugtai',
            field=models.IntegerField(default=0, verbose_name='\u5ba1\u6838\u72b6\u6001', choices=[(0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u901a\u8fc7'), (2, '\u5df2\u62d2\u7edd')]),
        ),
    ]
