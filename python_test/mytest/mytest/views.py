from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
import MySQLdb
from books.models import Book

def hello(request):
    return HttpResponse('Hello World Hi')

def my_homepage_view(request):
    return HttpResponse('home')
    
def current_datetime(request):
    #now = datetime.datetime.now()
    #return render_to_response('current_datetime.html', {'current_date': now})

    current_date = datetime.datetime.now()
    current_section = "op"
    i = range(10)
    #print i
    return render_to_response('current_datetime.html', locals())
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
    return render_to_response('hours_ahead.html', locals())
#    assert False
    #html = "<html><body>In %s hour(s), it will be %s.</html></body>" % (offset, dt)
    #html = "<html><body>In %s hour(s), it will be %s.</html></body>" % (offset, dt)
    #return HttpResponse(html)
    

def book_list(request):
    #db = MySQLdb.connect(user='root', db='orange', passwd='rootroot', host='localhost', unix_socket='/tmp/mysql.sock')
    db = MySQLdb.connect(user='root', db='orange', passwd='rootroot', host='127.0.0.1')
    cursor = db.cursor()
    cursor.execute('select * from test002')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})

def current_url_view_bad(request):
	return HttpResponse("Welcome to the papge at /current/")

def current_url_view_good(request):
	return HttpResponse("Welcome to the goodpapge at %s" % request.path)


def ua_display_bad(request):
	ua = request.META['HTTP_USER_AGENT']
	return HttpResponse("your browser is %s" % ua)

def ua_display_good(request):
	try:
		ua = request.META['HTTP_USER_AGENT']
	except KeyError:
		ua = 'unknown'	
	return HttpResponse("your browser is %s" % ua)

def display_meta(request):
	values = request.META.items()	
	return render_to_response('display_meta.html', locals())

def search_form(request):
	return render_to_response('search_form.html')

#def search(request):
#	#if request.GET['q']:
#	#if request.GET['q'] in list1:
#	if 'q' in request.GET:
#	
#	#	print request.GET['q']
#		message = 'you searched for: %s' % request.GET['q']
#	#	return HttpResponse(message)
#    #elif not request.GET['q']:
#	#    message = 'i am false'
#	#elif  request.GET['q'] == ' ':
#	#	return render_to_response('search_form.html')		
#
#	else:
#		message = 'you subbitted an empty form.'
#	return HttpResponse(message)

def search(request):
	#if 'q' in request.GET and request.GET['q']:
	#error = False
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term')
		elif len(q) > 5:
			errors.append('please enter at most 5 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'book': books, 'query': q})
#	else:
	#	return HttpResponse('please submit a search term.')
	#else:
	#	return render_to_response('search_form.html', {'error': True})
	return render_to_response('search_form.html', {'errors': errors})

def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('enther a subject')
		if not request.POST.get('message', ''):
			errors.append('enther a message')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('enther a valid e-mail address.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
					)
			return HttpResponseRedirect('/contact/thank/')
	return render_to_response('contact_form.html', {'errors': errors, 'subject': request.POST.get('subject', ''), 'message': request.POST.get('message', ''), 'email': request.POST.get('email', ''),})
				
























