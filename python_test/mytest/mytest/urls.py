from django.conf.urls import patterns, include, url
from mytest.views import  hello, my_homepage_view, current_datetime, hour_ahead, book_list
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^$', my_homepage_view),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2}?)/$', hour_ahead),
    (r'^admin/$', include(admin.site.urls)),
    ('^booklist/$', book_list),
    #...
)
