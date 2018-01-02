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
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.groups.all()[0].id==1:
            return ['yonghuzhonglei']

        return super(ManageUserAdmin, self).get_readonly_fields(request,obj)
    def get_fields(self, request, obj=None):
        l=super(ManageUserAdmin, self).get_fields(request, obj)
        if not request.user.is_superuser and request.user.groups.all()[0].id==1:
            if "keshi_f" in l:
                l.remove("keshi_f")
            if obj.xuehao!="" and "gonghao" in l:
                l.remove("gonghao")
            if obj.gonghao!="" and "xuehao" in l:
                l.remove("xuehao")

        return l



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

    def get_actions(self, request):
        actions = super(MacHistoyAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('main.view_feedback'):
            return [f.name for f in self.model._meta.fields]

        return self.readonly_fields
    def has_delete_permission(self, request, obj=None):
        if obj:
            if obj.jiechuren!=request.user.manageuser or obj.shenhezhuanugtai!=0:
                return False
        return super(MacHistoyAdmin, self).has_delete_permission(request,obj)


@admin.register(models.Macinsh)
class MacinshAdmin(admin.ModelAdmin):
    list_display = ("name", "bianhao", "zhuangtai")
    search_fields = ["name", "bianhao", "xinghao"]


from django.contrib import admin
from django.contrib.auth.models import Permission


class CustomModelAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        opts = self.opts
        view_permission = 'view_%s' % self.model._meta.module_name
        return request.user.has_perm(opts.app_label + '.' + view_permission)

    def has_change_permission(self, request, obj=None):
        if hasattr(self, 'has_change'):
            if self.has_change:
                return True

        return super(CustomModelAdmin, self).has_change_permission(request, obj)

    def get_model_perms(self, request):
        value = super(CustomModelAdmin, self).get_model_perms(request)
        value['view'] = self.has_view_permission(request)
        return value

    def changelist_view(self, request, extra_context=None):
        if self.has_view_permission(request, None):
            self.has_change = True
        result = super(CustomModelAdmin, self).changelist_view(request, extra_context)
        self.has_change = False
        return result