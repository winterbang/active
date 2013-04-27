from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
from active.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),
    url(r'^statics/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^register/$',uregist),
    url(r'^user/home/(?P<user_id>\d+)/$',home),
    url(r'^user/user_info/$',user_info),
    url(r'^user/change_passwd/$',change_passwd),
    url(r'^user/face/$',face),
    url(r'^user/hold_act/$',hold_act),
    url(r'^logout/$',ulogout),

)
