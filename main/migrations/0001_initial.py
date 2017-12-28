# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='keshi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keshi', models.CharField(max_length=255, verbose_name='\u79d1\u5ba4')),
            ],
            options={
                'verbose_name': '\u79d1\u5ba4\u7ba1\u7406',
                'verbose_name_plural': '\u79d1\u5ba4\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='MacHistoy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jiechushijian', models.DateField(verbose_name='\u501f\u51fa\u65e5\u671f')),
                ('guihuanshijian', models.DateField(verbose_name='\u5f52\u8fd8\u65f6\u95f4')),
                ('shifouyuqi', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903e\u671f')),
                ('beizhu', models.CharField(max_length=255, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u501f\u51fa\u5386\u53f2',
                'verbose_name_plural': '\u501f\u51fa\u5386\u53f2',
            },
        ),
        migrations.CreateModel(
            name='Macinsh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u540d\u79f0')),
                ('bianhao', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u5b66\u6821\u56fa\u5b9a\u8d44\u4ea7\u7f16\u53f7')),
                ('xinghao', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u578b\u53f7', blank=True)),
                ('gongneng', models.CharField(max_length=255, verbose_name='\u529f\u80fd\u8bf4\u660e', blank=True)),
                ('zhuyishiqiang', models.CharField(max_length=255, verbose_name='\u6ce8\u610f\u4e8b\u9879', blank=True)),
                ('beizhu', models.CharField(max_length=255, verbose_name='\u5907\u6ce8', blank=True)),
                ('image', models.ImageField(upload_to=b'images', null=True, verbose_name='\u8bbe\u5907\u56fe\u7247', blank=True)),
                ('zhuangtai', models.IntegerField(default=0, verbose_name='\u8bbe\u5907\u72b6\u6001', choices=[(0, '\u5728\u5e93'), (1, '\u5f85\u5ba1\u6838'), (2, '\u501f\u51fa')])),
                ('keshi_f', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xa7\x91\xe5\xae\xa4', to='main.keshi')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u7ba1\u7406',
                'verbose_name_plural': '\u8bbe\u5907\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ManageUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u59d3\u540d', blank=True)),
                ('xuehao', models.CharField(max_length=255, verbose_name='\u5b66\u53f7', blank=True)),
                ('gonghao', models.CharField(max_length=255, verbose_name='\u5de5\u53f7', blank=True)),
                ('shouji', models.CharField(max_length=255, verbose_name='\u624b\u673a')),
                ('youxiang', models.CharField(max_length=255, verbose_name='\u90ae\u7bb1')),
                ('yonghuzhonglei', models.IntegerField(default=0, verbose_name='\u7528\u6237\u79cd\u7c7b', choices=[(1, b'\xe7\x94\xa8\xe6\x88\xb7'), (2, b'\xe7\xa7\x91\xe5\xae\xa4\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98'), (3, b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')])),
                ('keshi_f', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xa7\x91\xe5\xae\xa4', to='main.keshi')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='machistoy',
            name='jiechuren',
            field=models.ForeignKey(related_name='re_jiechuren', verbose_name=b'\xe5\x80\x9f\xe5\x87\xba\xe4\xba\xba', to='main.ManageUser'),
        ),
        migrations.AddField(
            model_name='machistoy',
            name='mac_f',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\x80\x9f\xe6\x9c\xba\xe5\x99\xa8', to='main.Macinsh'),
        ),
        migrations.AddField(
            model_name='machistoy',
            name='shenheren',
            field=models.ForeignKey(related_name='re_shenheren', verbose_name=b'\xe5\xae\xa1\xe6\xa0\xb8\xe4\xba\xba', to='main.ManageUser'),
        ),
    ]
