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
    with open(templateFile) as fp:		#�}�Һ����d���ɡA�إ߽d��
        t = template.Template(fp.read())
        
    current_name = choice(names)		#�H����ܤ@�ӰݭԤH
    h = datetime.datetime.now().hour	#�ثe�ɶ�
    if 0<=h<12:						#�W��
        mae = 'Morning'
    elif 12<=h<18:					#�U��
        mae = 'Afternoon'
    else:							#�ߤW
        mae = 'Evening'
    con = template.Context({'name':current_name, 'morning_afternoon_evening':mae})
    html = t.render(con)				#��V�d��
    return HttpResponse(html)
