from time import time
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User  
from .models import UserProfile


class LoginForm(forms.Form):
	username = forms.fields.CharField(max_length=30)
	password = forms.fields.CharField(max_length=30)

class RegisterForm(forms.Form):
	username = forms.fields.CharField(max_length=30)
	password = forms.fields.CharField(max_length=30)
	confirm_password = forms.fields.CharField(max_length=30)
	email = forms.fields.EmailField(max_length=30)

	def clean(self):
		if self.cleaned_data['password']\
		!= self.cleaned_data['confirm_password']:
			raise ValidationError('两次输入密码不一致')
		else:
			self.cleaned_data.pop('confirm_password')
		return self.cleaned_data

class CustomFileInput(forms.FileInput):
	'''
		why not work?
	'''
	class Media:
		css = {
			'all' : ('css/profile_edit.html',),
		}
		js = ('js/jquery-3.3.1.min.js',)


class UserProfileEditForm(forms.Form):
	nickname = forms.fields.CharField(max_length=30,label="昵称")
	photo = forms.fields.ImageField(
		widget=CustomFileInput(
			# attrs={
			# 	'style':'overflow:hidden;width:100%;height:100%;'
			# }
			),
		)
	number = forms.fields.CharField(
			max_length=11,
			widget=forms.NumberInput,
			validators=[
				RegexValidator(r'^[0-9]{1,11}$', 'Enter a valid phone number.')
			],
			label='手机号码',
		)
	def __init__(self,*arg,**kwarg):
		if 'user' in kwarg:
			self.user = kwarg.pop('user')
		super(UserProfileEditForm,self).__init__(*arg,**kwarg)


	def clean(self):
		filename = self.cleaned_data['photo'].name
		self.cleaned_data['photo'].name = self.user.username + str(time())+ '.' +filename.split('.')[-1]
		try:
			self.user.userprofile.nickname = self.cleaned_data['nickname']
			self.user.userprofile.photo = self.cleaned_data['photo']
			self.user.userprofile.number = self.cleaned_data['number']
			self.user.userprofile.save()
		except User.userprofile.RelatedObjectDoesNotExist:
			temp = self.cleaned_data
			temp['user'] =self.user
			up = UserProfile.objects.create(**temp)
			if not up:
				raise ValidationError('创建用户失败')
		return self.cleaned_data


