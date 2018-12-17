# from django.db.models.fields import exceptions as db_e
from django.contrib.contenttypes.models import ContentType
from .models import ReadCount
from django.shortcuts import render

class GetReadInfo():
	def get_read_num(self):
		try:
			ct = ContentType.objects.get_for_model(self)
			rm = ReadCount.objects.get(content_type=ct,object_id=self.id)
			return rm.read_count
		except Exception as e:
			return 0

def order_by_read_num(model,obj_id_list):
	ordered_obj_id = []
	try:
		ct = ContentType.objects.get_for_model(model)
		rm_id_list = ReadCount.objects.filter(content_type=ct,object_id__in=obj_id_list).order_by('read_count').values('object_id')
		for rm in rm_id_list:
			if len(ordered_obj_id) < 10:
				ordered_obj_id.append(rm['object_id'])
	except Exception as e:
		pass
	return ordered_obj_id

			



def set_read_return_response(req,blog,context):
	key = 'blog_%s_reades' % blog.id
	if not req.COOKIES.get(key):
		try:
			ct = ContentType.objects.get_for_model(blog)
			read = ReadCount.objects.get(content_type=ct,object_id=blog.id)
			read.read_count += 1
		except Exception as e:
			ct = ContentType.objects.get_for_model(blog)
			read = ReadCount.objects.create(content_type=ct,object_id=blog.id,read_count=1)
		read.save()
		response = render(req,'blog/detail.html',context)
		response.set_cookie(key,'true')
		return response
	else:
		response =render(req,'blog/detail.html',context)
		return response