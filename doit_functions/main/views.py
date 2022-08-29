import json

from django.shortcuts import render,redirect
import requests

from main.models import Review


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

    subjects = [
        ('내과'),('정신의학과'),
        ('외과'),
        ('정형외과'),
        ('신경외과'),
        ('흉부외과'),
        ('마취통증의학과'),
        ('산부인과'),
        ('소아청소년과'),
        ('이비인후과'),
        ('영상의학과'),
        ('병리과'),
        ('가정의학과'),
        ('치과보철과'),
        ('치과교정과'),
        ('치주과'),
    ]

    # 병원api
    url = f'https://open.jejudatahub.net/api/proxy/tbb1D1a1559at91ababaata1abtba58a/{your_appkey}?openStatus={status}&bizSmallType={bizSmallType}&limit=100'

    response = requests.get(url)
    data = response.json()

    context={
        'selected_locations': selected_locations,
        'data':data,
        'subjects':subjects
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
    data2 = sorted(data['data'], key=lambda x: x['updateAt'], reverse=True)
    data['data'] = data2

    # 저장후 불러오기
    hospital_reples = Review.objects.filter(companyName=name)

    context={
        'data':data,
        'hospital_reples':hospital_reples,
    }
    return render(request,'hospitaldetail.html',context)


def comment(request):
    jsonOject = json.loads(request.body)

    companyName=jsonOject.get('companyName')
    
    # db에 저장
    reple = Review.objects.create(
        user_id=jsonOject.get('user_id'),
        title=jsonOject.get('title'),
        content=jsonOject.get('content'),
        star=jsonOject.get('star'),
        companyName=jsonOject.get('companyName'),
        licenseDate=jsonOject.get('licenseDate'),
    )

    return redirect('hospitaldetail', name=companyName)
