#coding:utf-8
from django import forms
import datetime

from django.forms import DateInput

from main.models import Macinsh


class addForm(forms.Form):
    jiechushijian=forms.DateField(label=u'借出时间',widget=DateInput({"class":"vDateField"}))
    guihuanshijian = forms.DateField(label=u'归还时间',widget=DateInput({"class":"vDateField"}))
    beizhu = forms.CharField(label=u'备注')

class macForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(macForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            for i in self.fields:

                self.fields[i].widget.attrs['readonly'] = True
                self.fields[i].widget.attrs['disabled'] = "disabled"
    class Meta:
        model=Macinsh
        exclude=("image",)

