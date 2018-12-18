from django.http import JsonResponse
from django.shortcuts import render_to_response,render
from reading_statistics.utils import get_read_quantum_in_days
from blog.models import Blog


def home_page(req):
	context = {}
	context['user'] = req.user
	context['active_app'] = req.resolver_match.url_name
	return render_to_response('index.html',context)

def graph_info(req):
	data = {}
	data['read_quantum'] = get_read_quantum_in_days(Blog,7)
	return JsonResponse(data)