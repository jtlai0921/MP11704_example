from django.http import HttpResponse, Http404
from math import sqrt

def isPrime(request, number):			#number��ܱ������Ѽ�
    try:
        number = int(number)
    except:
        raise Http404
    if number == 2:					#2�O�̤p�����
        flag = ' is '
    else:
        for i in range(2, int(sqrt(number)+2)):	#�P�_number�O�_�����
            if number%i == 0:
                flag = ' is not '
                break
        else:
            flag = ' is '
    txt = str(number)+flag+' a Prime'
    return HttpResponse('<h1>'+txt+'</h1>')
