# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171228_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machistoy',
            name='shenheren',
            field=models.ForeignKey(related_name='re_shenheren', verbose_name=b'\xe5\xae\xa1\xe6\xa0\xb8\xe4\xba\xba', blank=True, to='main.ManageUser', null=True),
        ),
    ]
