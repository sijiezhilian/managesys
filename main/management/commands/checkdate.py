import datetime
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

# Now this script or any imported module can use any part of Django it needs.





class Command(BaseCommand):
    def handle(self, *args, **options):
        import django
        from django.conf import settings
        from managesys import settings
        print "hello"
        # settings.configure(default_settings=settings, DEBUG=True)
        # django.setup()
        # from main.models import MacHistoy
        # end_date = datetime.date.today() + datetime.timedelta(days=5)
        # h = MacHistoy.objects.filter(guihuanshijian__lte=end_date)
        # print len(h)
        # for i in h:
        #     i.shifouyuqi = False
        #     i.save()
        #

    def sendmail(to, content):
        send_mail(content, content, 'p564398853@163.com',
                  to, fail_silently=False)