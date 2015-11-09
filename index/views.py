from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import redirect
from .config import *
from .forms import CustomerForm
import traceback

# Create your views here.
def index_view(request):
    flog.info("PV, index, ")
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('index/index.html')
    return HttpResponse(template.render(context))

def login_view(request):
    flog.info("PV, login, ")
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('index/login.html')
    return HttpResponse(template.render(context))
def login_handler_view(request):
    flog.info("PV, login_handler, ")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                # Return a 'disabled account' error message ...
                return HttpResponse('Error, disable account')
        else:
            # Return an 'invalid login' error message. ...
            return HttpResponse('Error, invalid login')
    return HttpResponse('Error')

def register_view(request):
    flog.info("PV, register, ")
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('index/register.html')
    return HttpResponse(template.render(context))
def register_handler_view(request):
    flog.info("PV, register_handler, ")
    if request.method == 'POST':
        ctx = {}

        form = CustomerForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Error:\n %s' % form.errors)
        try:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            # create user
            u = User.objects.create_user(username, email, password)
            profile = u.profile
            profile.jituanming = form.cleaned_data['jituanming']
            profile.dianming = form.cleaned_data['dianming']
            profile.chengshiming = form.cleaned_data['chengshiming']
            profile.daqu = form.cleaned_data['daqu']
            profile.xiaoqu = form.cleaned_data['xiaoqu']
            profile.chengshijibie = form.cleaned_data['chengshijibie']
            profile.dizhi = form.cleaned_data['dizhi']
            profile.dianhua = form.cleaned_data['dianhua']
            profile.save()

            ctx['u'] = u
        except Exception, e:
            err = traceback.format_exc()
            return HttpResponse(err)

        ctx = {}
        ctx['form'] = form
        context = RequestContext(request, ctx)
        template = loader.get_template('index/register_handler.html')
        return HttpResponse(template.render(context))
    return HttpResponse('Error')

def logout_view(request):
    flog.info("PV, logout, ")
    logout(request)
    return redirect('/')
