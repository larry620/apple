from django.conf.urls import patterns, include, url
from mytest.views import  hello, my_homepage_view, current_datetime, hour_ahead


urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^$', my_homepage_view),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2}?)/$', hour_ahead),
    #...
)