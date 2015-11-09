
from django import forms
from django.forms import ModelForm

#from .models import Customer

class CustomerForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    password = forms.CharField(label='password', max_length=32)
    email = forms.CharField(label='email', max_length=32)

    jituanming = forms.CharField(label='jituanming', max_length=32)
    dianming = forms.CharField(label='dianming', max_length=32)
    chengshiming = forms.CharField(label='chengshiming', max_length=32)
    chengshijibie = forms.CharField(label='chengshijibie', max_length=32)
    daqu = forms.CharField(label='daqu', max_length=32)
    xiaoqu = forms.CharField(label='xiaoqu', max_length=32)
    dizhi = forms.CharField(label='dizhi', max_length=32)
    dianhua = forms.CharField(label='dianhua', max_length=32)

class PickupForm(forms.Form):
    location = forms.CharField(label='location', max_length=32)
    service = forms.CharField(label='service', max_length=32)
    car = forms.CharField(label='car', max_length=64)
    date = forms.CharField(label='date', max_length=64)
    flight = forms.CharField(label='flight', max_length=64)
    fname = forms.CharField(label='fname', max_length=64)
    email = forms.CharField(label='email', max_length=64)
    destination = forms.CharField(label='destination', max_length=512)

