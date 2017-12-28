#coding:utf-8

from django.core.mail import send_mail
from main.models import *
import datetime

def sendmail(to,content):
    send_mail(content, content, 'p564398853@163.com',
              to, fail_silently=False)
def check():


    end_date = datetime.date.today()+datetime.timedelta(days=5)
    h=MacHistoy.objects.filter(guihuanshijian__lte=end_date)
    print len(h)
    for i in h:

        i.shifouyuqi=False
        i.save()

        sendmail([i.jiechuren.youxiang,i.shenheren.youxiang],i.jiechuren.name+u"租借时间要到期了请注意")
