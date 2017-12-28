# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_machistoy_shenhezhuanugtai'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machistoy',
            options={'verbose_name': '\u501f\u51fa\u4fe1\u606f', 'verbose_name_plural': '\u501f\u51fa\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='machistoy',
            name='shenhezhuanugtai',
            field=models.IntegerField(default=0, verbose_name='\u5ba1\u6838\u72b6\u6001', choices=[(0, '\u5f85\u5ba1\u6838'), (1, '\u5ba1\u6838\u901a\u8fc7'), (2, '\u5df2\u5f52\u8fd8'), (3, '\u5df2\u62d2\u7edd')]),
        ),
        migrations.AlterField(
            model_name='macinsh',
            name='zhuangtai',
            field=models.IntegerField(default=0, verbose_name='\u8bbe\u5907\u72b6\u6001', choices=[(0, '\u5728\u5e93'), (1, '\u501f\u51fa')]),
        ),
        migrations.AlterField(
            model_name='manageuser',
            name='youxiang',
            field=models.EmailField(max_length=255, verbose_name='\u90ae\u7bb1', blank=True),
        ),
    ]
