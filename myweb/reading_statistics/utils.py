# from django.db.models.fields import exceptions as db_e
from django.utils import timezone
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


def model_order_by_read_num(model):
    '''
        give a model return a read statistic TOP 10 models list
    '''
    today = timezone.now().today()
    m = today.month
    y = today.year
    month_start_day = timezone.datetime(year=y,month=m,day=1)
    objs = model.objects.filter(read_statistics__create_time__gt=month_start_day)\
                .order_by('-read_statistics__read_count')\
                .values('id','theme','read_statistics__read_count')
    return objs
    try:
        ct = ContentType.objects.get_for_model(model)
        rm_id_list = ReadCount.objects.filter(content_type=ct,create_time__gt=month_start_day)\
                    .order_by('-read_count').values_list('object_id')[:10]
        objs = []
        for i in rm_id_list:
            obj = model.objects.get(id=i[0])
            objs.append(obj)
        return objs
    except Exception as e:
        return []

            
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