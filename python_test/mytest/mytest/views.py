#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
def hello(request):
    return HttpResponse('Hello World Hi')

def my_homepage_view(request):
    return HttpResponse('home')
    
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
    #t = get_template('current_datetime.html')
#    t = Template("<html><body> It is now {{current_date}}.</body></html>")
    #html = t.render(Context({'current_date': now}))
#    html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    
def hour_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False
    html = "<html><body>In %s hour(s), it will be %s.</html></body>" % (offset, dt)
    return HttpResponse(html)
    