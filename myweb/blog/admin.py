from django.contrib import admin
from . import models
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	"""docstring for BlogAdmin"""
	list_display = ('id','theme','update','get_read_num','user')
	
	class Meta:
		ordering = ['-update']

	def __str__(self):
		return self.theme


admin.site.register(models.Blog,BlogAdmin)