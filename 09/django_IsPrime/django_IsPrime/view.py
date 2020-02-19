from django.http import HttpResponse, Http404
from math import sqrt

def isPrime(request, number):			#number表示接收的參數
    try:
        number = int(number)
    except:
        raise Http404
    if number == 2:					#2是最小的質素
        flag = ' is '
    else:
        for i in range(2, int(sqrt(number)+2)):	#判斷number是否為質素
            if number%i == 0:
                flag = ' is not '
                break
        else:
            flag = ' is '
    txt = str(number)+flag+' a Prime'
    return HttpResponse('<h1>'+txt+'</h1>')
