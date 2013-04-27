# Create your views here.
from active.forms import *
from active.models import *
from django.shortcuts import render,redirect


def index(req):



    return render(req,'index.html',{})


def uregist(req):
    if req.method=="POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            un = uf.cleaned_data['username']
            pa = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            User.objects.create_user(un,email,pa)
            return redirect('//')
    else:
        pass
        uf=UserForm()
        zidian={'uf':uf}
    return render(req,'register.html',zidian)
def ulogin(req):
    pass


def home(req):
    pass


def user_info(req):
    pass




def face(req):
    pass



def change_passwd(req):
    pass

def hold_act(req):


    pass









