# Create your views here.
from active.forms import *
from active.models import *
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(req):
    if req.method=="POST":
        lf = LoginForm(req.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username'] 
            password = lf.cleaned_data['password']
            user = authenticate(username = username,password=password)
            if user is None:
                return redirect('/index/')
            else :
                if req.META.has_key('HTTP_X_FORWARDED_FOR'):
                    ip = req.META['HTTP_X_FORWARDED_FOR']
                else:
                    ip = req.META['REMOTE_ADDR']
                login(req,user) 
                up = UserProfile.objects.get(user=user)
		up.ip=ip
                up.save()
		return render(req,'index.html',{'user':req.user})       
    else:
        lf = LoginForm()
    zidian={'lf':lf}
    return render(req,'index.html',zidian)

    


def uregist(req):
    if req.method=="POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            un = uf.cleaned_data['username']
            pa = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            print un,pa,email
            user = User.objects.create_user(un,email,pa)
            UserProfile.objects.create(user=user)
            return redirect('/index/')
    else:
        lf=LoginForm() 
        uf=UserForm()
        zidian={'uf':uf,'lf':lf}
    return render(req,'register.html',zidian)
    


def home(req,user_id):
    if req.user.is_authenticated():
        user = User.objects.get(id__exact=user_id)
        print user.date_joined
        print user.last_login
        up = UserProfile.objects.get(user=user)
        return render(req,'home.html',{'user':user,'up':up})
    else:
        return redirect('/index/')

def user_info(req):
    if req.method=='POST':
        pass 
    else:
        if req.user.is_authenticated():
            zidian={'user':req.user}
            return render(req,'user_info.html',zidian)
        else :
            return redirect('/index/')



def face(req):
    if req.method=="POST":
        hdimg = req.FILES.get('hdimg','')
        print hdimg
        if hdimg:
            user = UserProfile.objects.get(user=req.user)
            user.headimg=hdimg
            user.save()
            pd=2
        else:
            pd=1
        uf=UserProfile.objects.get(user__exact=req.user)
        zidian={'pd':pd,'user':req.user,'uf':uf}
        return render(req,'face.html',zidian)
    else:
        if req.user.is_authenticated():
            pd=0
            zidian={'user':req.user,'pd':pd}
            return render(req,'face.html',zidian)
        else:
            return redirect('/index/')



def change_passwd(req):
    if req.method=="POST":
        user = User.objects.get(username=req.user.username)
        passwd = req.POST.get('oldpswd','')
        if user.check_password(passwd):
            pd1 = req.POST.get('newpswd1','')
            pd2 = req.POST.get('newpswd2','')
            if pd1 == pd2:
                user.set_password(pd1)
                user.save()
                pd=3
            else:
                pd=2
        else:
            pd=1
        zidian={'user':user,'pd':pd}
        return render(req,'change_passwd.html',zidian)
    else:
        if req.user.is_authenticated():
            pd=0
            zidian={'user':req.user,'pd':pd}
            return render(req,'change_passwd.html',zidian)
        else:
            return redirect('/index/')

def hold_act(req):
    if req.method=='POST':
        pass    
    else:
        if req.user.is_authenticated():    
            zidian={'user':req.user}
            return render(req,'hold_act.html',zidian)
        else:
            return redirect('/index/')
    








def ulogout(req):
    logout(req)
    return redirect('/index/')
