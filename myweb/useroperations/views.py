from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.http import require_POST,require_http_methods,require_GET
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm,RegisterForm,UserProfileEditForm
from .models import UserProfile
# Create your views here.

@require_http_methods(['POST','GET'])
def acc_login(req):
	context = {}
	if req.method == 'GET':
		form  = LoginForm()
		context['from'] = form
		return render(req,'user/login.html',context)
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
		return render(req,'user/login.html',context)


@require_GET
def acc_logout(req):
	logout(req)
	return redirect('login')

@require_http_methods(['POST','GET'])
def acc_register(req):
	context= {}
	if req.method == 'GET':
		return render(req,'user/register.html')
	else:
		form = RegisterForm(req.POST)
		if form.is_valid():
			try:
				user = User.objects.create_user(**form.cleaned_data)
			except Exception as e:
				context['erro'] ='注册错误'
				return render(req,'user/register.html',context)
			else:
				user.save()
				login(req,user)
			return redirect('blog')
		return render(req,'user/register.html',context)

@require_GET		
@login_required
def user_personal_center(req):
	context = {}
	return render(req,'user/user_personal_center.html',context)

@login_required
def profile_edit(req):
	context = {}
	if req.method == 'GET':
		try:
			up = req.user.userprofile
			initial = {
				'nickname':up.nickname,
				'number':up.number,
			}
			profile_form = UserProfileEditForm(initial=initial)
		except User.userprofile.RelatedObjectDoesNotExis:
			profile_form = UserProfileEditForm()
		context['profile_form'] = profile_form
	else:
		profile_form = UserProfileEditForm(req.POST,req.FILES,user=req.user)
		if profile_form.is_valid():
			return HttpResponse('<script>settimeout(window.location.reload(),3)</script>')
		else:
			context['profile_form'] = profile_form
	return render(req,'user/profile_edit.html',context)