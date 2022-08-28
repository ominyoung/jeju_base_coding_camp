from multiprocessing import context
from django.shortcuts import render
import requests

your_appkey = '6614t13ct60404b1333jr04t3r41_c60'
status = '영업/정상'
bizSmallType='병원'

def index(request):
    locations = [
        ('Hangyeong-myeon', '한경면'), 
        ('Hallim-eup', '한림읍'),
        ('Aewol-eup', '애월읍'), 
        ('Jeju-si', '제주시'), 
        ('Jocheon-eup', '조천읍'), 
        ('Gujwa-eup', '구좌읍'),
        ('Daejeong-eup', '대정읍'),
        ('Andeok-myeon', '안덕면'),
        ('Seogwipo-si', '서귀포시'),
        ('Namwon-eup', '남원읍'),
        ('Pyoseon-myeon', '표선면'),
        ('Seongsan-eup', '성산읍'),
        ('Udo-myeon', '우도면'),
    ]
    context = {
        'locations':locations
    }
    return render(request, 'index.html', context)


def hospitallist(request):
    selected_locations = request.GET.getlist('locations')

    # 병원api
    url = f'https://open.jejudatahub.net/api/proxy/tbb1D1a1559at91ababaata1abtba58a/{your_appkey}?openStatus={status}&bizSmallType={bizSmallType}&limit=100'

    response = requests.get(url)
    data = response.json()

    context={
        'selected_locations': selected_locations,
        'data':data,
    }
    return render(request, 'hospitallist.html', context)

def hospitaldetail(request, name):
    print(name)

    # 병원api
    url = f'https://open.jejudatahub.net/api/proxy/tbb1D1a1559at91ababaata1abtba58a/{your_appkey}?openStatus={status}&bizSmallType={bizSmallType}&companyName={name}'

    response = requests.get(url)
    data = response.json()

    # 데이터가 종종 update날짜만 다른 2개 이상인 값이 있음 ex) 서귀포열린병원
    # update 날짜가 최신인 것만 취급
    print(dir(data['data']))
    data2 = sorted(data['data'], key=lambda x: x['updateAt'], reverse=True)
    data['data'] = data2

    context={
        'data':data
    }
    return render(request,'hospitaldetail.html',context)
