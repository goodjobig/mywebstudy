from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.http import require_POST,require_http_methods,require_GET
from django.contrib.auth.models import User
from .forms import LoginForm
from .forms import RegisterForm
# Create your views here.

@require_http_methods(['POST','GET'])
def acc_login(req):
	context = {}
	if req.method == 'GET':
		form  = LoginForm()
		context['from'] = form
		return render(req,'login.html',context)
	else:
		form = LoginForm(req.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user:
				login(req,user)
				return redirect('blog')
			else:
				context['erro'] = '用户名或密码错误'
		return render(req,'login.html',context)


@require_GET
def acc_logout(req):
	logout(req)
	return redirect('login')

@require_http_methods(['POST','GET'])
def acc_register(req):
	context= {}
	if req.method == 'GET':
		return render(req,'register.html')
	else:
		form = RegisterForm(req.POST)
		if form.is_valid():
			try:
				user = User.objects.create_user(**form.cleaned_data)
			except Exception as e:
				context['erro'] ='注册错误'
				return render(req,'register.html',context)
			else:
				user.save()
				login(req,user)
			return redirect('blog')
		return render(req,'register.html',context)
		