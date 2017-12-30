#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
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

        return render(request, "ex_change_form.html", {"form": addForm().as_ul(), "mgroup": a})
    if request.method == "POST":
        form = addForm(request.POST)
        id = request.GET.get("id")
        mac = Macinsh.objects.get(id=id)
        if form.is_valid():
            jiechushijian = form.cleaned_data['jiechushijian']
            guihuanshijian = form.cleaned_data['guihuanshijian']
            beizhu = form.cleaned_data['beizhu']
            MacHistoy.objects.create(mac_f=mac,
                                     jiechushijian=jiechushijian,
                                     guihuanshijian=guihuanshijian,
                                     beizhu=beizhu,
                                     jiechuren=request.user.manageuser
                                     )
        else:
            return HttpResponseBadRequest(u"error")
        return HttpResponseRedirect('/main/')


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
                                   yonghuzhonglei=1
                                   )

        man.user.set_password(password)
        man.user.save()
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)

        return HttpResponseRedirect(request.GET.get("next_to", '/main/'))