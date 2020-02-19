from django.http import HttpResponse, Http404
import datetime
from django import template
from django.conf import settings
import os
import os.path
from random import choice

#settings.configure()
names = ('Zhang san', 'Li si', 'Wang wu', 'Ma liu')

def greeting(request):
    templateFile = os.path.join(os.path.split(os.path.dirname(__file__))[0],\
        'templates') + '\\greeting.html'
    with open(templateFile) as fp:		#開啟網頁範本檔，建立範本
        t = template.Template(fp.read())
        
    current_name = choice(names)		#隨機選擇一個問候人
    h = datetime.datetime.now().hour	#目前時間
    if 0<=h<12:						#上午
        mae = 'Morning'
    elif 12<=h<18:					#下午
        mae = 'Afternoon'
    else:							#晚上
        mae = 'Evening'
    con = template.Context({'name':current_name, 'morning_afternoon_evening':mae})
    html = t.render(con)				#渲染範本
    return HttpResponse(html)
