#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.template import RequestContext
from django.contrib import auth
from django.core import serializers
from models import *
from form import *

import datetime

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        yzm = request.POST.get("yzm", '')
        # if yzm is not '22828':
        #     return render(request, 'index.html', {'zym_is_wrong': True})
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)

            return HttpResponseRedirect(request.GET.get("next_to", '/main/'))

        else:
            return render(request, 'index.html', {'password_is_wrong': True})


@login_required
def sysmain(request):

    zhuangtai = request.GET.get("status", 0)
    q = request.GET.get("q", None)

    contact_list = Macinsh.objects.filter(zhuangtai=zhuangtai)
    if (q != None):
        contact_list = contact_list.filter(Q(name=q) | Q(bianhao=q) | Q(xinghao=q))
    paginator = Paginator(contact_list, 8)  # Show 25 contacts per page

    try:
        a = request.user.groups.all()[0].id
    except IndexError:
        a = 1
    page = request.GET.get('page', 1)
    try:
        # a = request.user.groups.all()[0].id
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {"Len": paginator.num_pages, "machines": contacts, "mgroup": a})


@login_required
def new_form(request):
    if request.method == "GET":
        try:
            a = request.user.groups.all()[0].id
        except IndexError:
            a = 1
        id=request.GET.get("id")
        q=Macinsh.objects.get(id=id)
        b='''
        <link type="text/css" href="http://code.jquery.com/ui/1.9.1/themes/smoothness/jquery-ui.css" rel="stylesheet" />

    <link href="../static/main/css/jquery-ui-timepicker-addon.css" type="text/css" />
    <script src="http://code.jquery.com/jquery-1.8.2.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="http://code.jquery.com/ui/1.9.1/jquery-ui.min.js"></script>
    <script src="../static/main/js/jquery-ui-timepicker-addon.js" type="text/javascript"></script>


    <script src="../static/main/js/zn.js" type="text/javascript"></script>

    <script type="text/javascript">

        jQuery(function () {
            jQuery('#id_jiechushijian').datepicker({

                dateFormat: "yy-mm-dd"
            });

        });
        jQuery(function () {
            jQuery('#id_guihuanshijian').datepicker({
                dateFormat: "yy-mm-dd"
            });

        });

    </script>
        <style type="text/css">
  ul, li {
    list-style: none;
    margin: 0;


}
    li{
        margin-bottom: 20px;
    }
    form li
    {display: inline-block;}

  </style>
         <form method="post" style="text-align: left;padding-top: 30px;padding-left: 30px ;list-style: none;
    margin: 0;">
            %s
                <input type="submit"/>
            </form>
            <div style="text-align: left;padding-top: 30px;padding-left: 30px ;list-style: none;margin: 0;">
            <img src="%s" style="height: 200px;
      width: 200px;"></img>
            %s
            <div>
        '''%(addForm().as_ul(),q.image.url,macForm(instance=q).as_ul())
        return HttpResponse(b)
    if request.method == "POST":
        form = addForm(request.POST)
        id = request.GET.get("id")
        mac = Macinsh.objects.get(id=id)
        if form.is_valid():
            jiechushijian = form.cleaned_data['jiechushijian']
            guihuanshijian = form.cleaned_data['guihuanshijian']
            beizhu = form.cleaned_data['beizhu']

            c=MacHistoy.objects.create(mac_f=mac,
                                     jiechushijian=jiechushijian,
                                     guihuanshijian=guihuanshijian,
                                     beizhu=beizhu,
                                     jiechuren=request.user.manageuser

                                     )

        else:
            return HttpResponseBadRequest(u"error")
        return HttpResponse('提交成功')


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")
def ifm(request):
    return render(request,'ifm.html')

def resign(request):
    if request.method == "GET":

        return render(request,'resign.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        shouji=request.POST.get("shouji")
        password = request.POST.get('password')
        youxiang=request.POST.get('youxiang',"")
        xingming=request.POST.get('xingming',"")
        xuehao=request.POST.get('xuehao',"")
        gonghao=request.POST.get('gonghao','')



        if(User.objects.filter(username=username).exists()):
            return render(request,'resign.html',{"username_is_exists":True})

        man=ManageUser.objects.create(yonghuming=username,
                                   youxiang=youxiang,
                                   name=xingming,
                                   xuehao=xuehao,
                                   gonghao=gonghao,
                                      shouji=shouji,
                                   yonghuzhonglei=1
                                   )

        man.user.set_password(password)
        man.user.save()
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)

        return HttpResponseRedirect(request.GET.get("next_to", '/main/'))