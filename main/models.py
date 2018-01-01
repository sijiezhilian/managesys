#coding:utf-8

from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
from mail import sendmail


class keshi(models.Model):
    keshi=models.CharField(u"科室",max_length=255)

    def __unicode__(self):
        return self.keshi

    class Meta:
        verbose_name = u"科室管理"
        verbose_name_plural = u"科室管理"
class ManageUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    yonghuming=models.CharField(u"用户名",help_text="只能为英文和数字。默认密码123456",max_length=50)
    name=models.CharField(u'姓名',max_length=255,blank=True)
    xuehao=models.CharField(u'学号',max_length=255,blank=True)
    gonghao=models.CharField(u"工号",max_length=255,blank=True)
    shouji=models.CharField(u"手机",max_length=255)
    youxiang=models.EmailField(u"邮箱",max_length=255,blank=True)
    yonghuzhongleichoic = ((1, "用户"), (2, "科室管理员"), (3, "系统管理员"))
    keshi_f=models.ForeignKey(keshi,verbose_name='所属科室',blank=True,null=True)
    yonghuzhonglei=models.IntegerField(u'用户种类',choices=yonghuzhongleichoic,default=0)

    class Meta:
        verbose_name = u"用户管理"
        verbose_name_plural = u"用户管理"

    def __unicode__(self):
        return self.name
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        user = User.objects.create_user(self.yonghuming, self.youxiang, '123456')
        self.user=user







        self.user.groups.clear()
        self.user.groups.add(Group.objects.get(id=self.yonghuzhonglei))

        self.user.is_staff = True

        self.user.save()

        return  models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                          update_fields=update_fields)


class Macinsh(models.Model):
    name=models.CharField(u"设备名称",max_length=255)
    bianhao=models.CharField(u"设备学校固定资产编号",max_length=255)
    xinghao=models.CharField(u"设备型号",max_length=255,blank=True)
    gongneng=models.CharField(u'功能说明',max_length=255,blank=True)
    zhuyishiqiang=models.CharField(u'注意事项',max_length=255,blank=True)
    beizhu = models.CharField(u'备注', max_length=255, blank=True)
    image=models.ImageField(u"设备图片",upload_to="images",blank=True,null=True)
    zhuangtaichoices=((0,u"在库"),(1,u'借出'))
    zhuangtai=models.IntegerField(u"设备状态",default=0,choices=zhuangtaichoices)
    keshi_f = models.ForeignKey(keshi, verbose_name='所属科室',blank=True,null=True)
    class Meta:
        verbose_name = u"设备管理"
        verbose_name_plural = u"设备管理"

    def __unicode__(self):
        return self.name
class MacHistoy(models.Model):
    jiechushijian = models.DateField(u'借出日期')
    guihuanshijian=models.DateField(u'归还时间')
    shifouyuqi=models.BooleanField(u'租借时间正常',default=True)
    shenhezhuanugtaichoice=((0,u"待审核"),(1,u"审核通过"),(2,u"已归还"),(3,u"已拒绝"))
    shenhezhuanugtai=models.IntegerField(u"审核状态",choices=shenhezhuanugtaichoice,default=0)
    beizhu=models.CharField(u"备注",max_length=255,blank=True)
    mac_f=models.ForeignKey(Macinsh,verbose_name='所借机器')
    jiechuren=models.ForeignKey(ManageUser,verbose_name='借出人',related_name="re_jiechuren")
    shenheren=models.ForeignKey(ManageUser,verbose_name="审核人",related_name="re_shenheren",blank=True,null=True)
    class Meta:
        verbose_name = u"借出信息"
        verbose_name_plural = u"借出信息"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.shenheren=self.mac_f.keshi_f.manageuser_set.all()[0]


        if self.shenhezhuanugtai==0:
            self.mac_f.zhuangtai=0
        if self.shenhezhuanugtai == 1:
            self.mac_f.zhuangtai = 1
        if self.shenhezhuanugtai == 2:
            self.mac_f.zhuangtai = 0
        if self.shenhezhuanugtai == 3:
            self.mac_f.zhuangtai = 0
        self.mac_f.save()
        if(self.shifouyuqi==True):
            sendmail([self.shenheren.youxiang],self.jiechuren.name+u"提交了申请请注意审核")
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)




    def __unicode__(self):
        return str(self.id)









