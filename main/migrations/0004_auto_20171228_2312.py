# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171228_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machistoy',
            name='shifouyuqi',
            field=models.BooleanField(default=True, verbose_name='\u79df\u501f\u65f6\u95f4\u6b63\u5e38'),
        ),
    ]
