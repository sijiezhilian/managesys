#coding:utf-8
from django import forms
import datetime

from django.forms import DateInput


class addForm(forms.Form):
    jiechushijian=forms.DateField(label=u'借出时间',widget=DateInput({"class":"vDateField"}))
    guihuanshijian = forms.DateField(label=u'归还时间',widget=DateInput({"class":"vDateField"}))
    beizhu = forms.CharField(label=u'备注')



