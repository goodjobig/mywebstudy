from django.shortcuts import render_to_response,render


def home_page(req):
	context = {}
	context['user'] = req.user
	context['active_app'] = req.resolver_match.url_name
	return render_to_response('index.html',context)