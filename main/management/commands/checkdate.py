#coding:utf-8
import datetime
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from main.models import MacHistoy as mach
# Now this script or any imported module can use any part of Django it needs.





class Command(BaseCommand):
    def handle(self, *args, **options):
        import django
        from django.conf import settings
        from managesys import settings



        end_date = datetime.date.today() + datetime.timedelta(days=5)
        h = mach.objects.filter(guihuanshijian__lte=end_date)
        print len(h)
        for i in h:

            i.shifouyuqi = False
            i.save()

            con=i.jiechuren.name+u"借出快到期了"

            send_mail(con, con, 'p564398853@163.com',
                      [i.jiechuren.youxiang, i.shenheren.youxiang], fail_silently=False)



    def sendmail(content,toa):
        send_mail(content, content, 'p564398853@163.com',
                  toa, fail_silently=False)