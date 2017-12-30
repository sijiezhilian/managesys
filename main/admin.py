#coding:utf-8
from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

import models
from import_export import resources

class hisResource(resources.ModelResource):
    jiechushijian=Field(attribute='jiechushijian',column_name=u'借出时间')
    guihuanshijian = Field(attribute='guihuanshijian', column_name=u'归还时间')
    jiechuren=Field(attribute='jiechuren',readonly=True,column_name=u'借出人',widget=ForeignKeyWidget(models.ManageUser, 'name'))
    shenheren = Field(attribute='shenheren',column_name=u'审核人',widget=ForeignKeyWidget(models.ManageUser, 'name'))
    mac_f=Field(attribute='mac_f',column_name=u'机器名',widget=ForeignKeyWidget(models.Macinsh, 'name'))
    beizhu= Field(attribute='beizhu', column_name=u'备注')
    class Meta:
        model = models.MacHistoy
        export_order = ('jiechushijian', 'guihuanshijian', 'beizhu', 'mac_f', "jiechuren", "shenheren",)
        fields = ('jiechushijian', 'guihuanshijian', 'beizhu', 'mac_f', "jiechuren", "shenheren",)
@admin.register(models.ManageUser)
class ManageUserAdmin(admin.ModelAdmin):
    exclude = ['user']
    list_display = ('yonghuming',"xuehao","gonghao","shouji","youxiang")
    search_fields=['yonghuming',"xuehao","gonghao","shouji","youxiang"]








@admin.register(models.keshi)
class KeshiAdmin(admin.ModelAdmin):
    list_display = ("keshi",)
    search_fields = ["keshi"]


@admin.register(models.MacHistoy)
class MacHistoyAdmin(ImportExportModelAdmin):
    resource_class=hisResource
    list_display = ("jiechushijian", "guihuanshijian", "shifouyuqi", "beizhu","jiechuren","shenheren","shenhezhuanugtai")
    search_fields = ["shifouyuqi", "beizhu","jiechuren","shenheren"]
    list_filter = (
        'shenhezhuanugtai',
        ('jiechushijian', DateRangeFilter),  # this is a tuple
        ('guihuanshijian', DateRangeFilter),
    )

@admin.register(models.Macinsh)
class MacinshAdmin(admin.ModelAdmin):
    list_display = ("name", "bianhao", "zhuangtai")
    search_fields = ["name", "bianhao", "xinghao"]
