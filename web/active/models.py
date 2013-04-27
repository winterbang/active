#!-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    headimg = models.FileField(upload_to='./headimg/')
    sex = models.CharField(max_length=1)
    user = models.ForeignKey(User,unique=True)
    birthday = models.DateTimeField()
    ip = models.CharField(max_length=20)
    fllowp = models.ManyToManyField(User,verbose_name=u'关注',null=True,related_name='fp')
    fllowa = models.ManyToManyField('Active',null=True)
    joina = models.ManyToManyField('Active',null=True,related_name="ja")    
    def fpnum():
        return self.fllowp.count()
    def fanum():
        return self.fllowa.count()
  


class Active(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    picture = models.FileField(upload_to='./picture/')
    leibie = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    time = models.DateTimeField()
    ifmoney = models.BooleanField()
    user = models.ForeignKey(User)
    

class Ackwd(models.Model):
    kword = models.CharField(max_length=30)
    active = models.ForeignKey(Active)

class Urkwd(models.Model):
    kword = models.CharField(max_length=30)
    user = models.ForeignKey(User)



class Actcmm(models.Model):
    content = models.TextField(u'内容')
    time = models.DateTimeField()
    user = models.ForeignKey(User)
    active = models.ForeignKey(Active)


class Say(models.Model):
    content = models.TextField(u'内容')
    time = models.DateTimeField()
    user = models.ForeignKey(User)


class Saycmm(models.Model):
    content = models.TextField(u'内容')
    time = models.DateTimeField()
    user = models.ForeignKey(User)
    say =  models.ForeignKey(Say)
   





    


     





