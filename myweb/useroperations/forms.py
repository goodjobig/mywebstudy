from django.forms import Form
from django.forms import fields
from django.core.exceptions import ValidationError
          

class LoginForm(Form):
	username = fields.CharField(max_length=30)
	password = fields.CharField(max_length=30)

class RegisterForm(Form):
	username = fields.CharField(max_length=30)
	password = fields.CharField(max_length=30)
	confirm_password = fields.CharField(max_length=30)
	email = fields.EmailField(max_length=30)

	def clean(self):
		if self.cleaned_data['password']\
		!= self.cleaned_data['confirm_password']:
			raise ValidationError('两次输入密码不一致')
		else:
			self.cleaned_data.pop('confirm_password')
		return self.cleaned_data