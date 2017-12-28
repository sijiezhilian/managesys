from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
import models



@admin.register(models.ManageUser)
class ManageUserAdmin(admin.ModelAdmin):
    list_display = ("xuehao","gonghao","shouji","youxiang")
    search_fields=["xuehao","gonghao","shouji","youxiang"]








@admin.register(models.keshi)
class KeshiAdmin(admin.ModelAdmin):
    list_display = ("keshi",)
    search_fields = ["keshi"]


@admin.register(models.MacHistoy)
class MacHistoyAdmin(admin.ModelAdmin):
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
