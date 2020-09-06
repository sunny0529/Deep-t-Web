#3. 동작을 하는 함수 만들기 : 함수는 deeptapp 안에 views.py 에서 정의해줄 수 있습니다.
#request가 들어왔을 때 home.html 을 불러주는 함수입니다.
#view 로 넘어가서 요청이 들어왔을 때 home.html 을 띄우도록 함수를 

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from django.shortcuts import render, redirect
from .deepfakeclassification import do
#render는 최대 3개의 인자까지 받을 수 있습니다.
#첫번째로 request, 두번째로 html 파일과 같은 템플릿, 마지막으로 dictionary 형 인자입니다.
#dictionary 형 인자는 파이썬 변수를 html 파일로 넘길 때 사용하는데 조금 이따 다뤄보도록 하겠습니다.
vid_status = 0
img_status = 0
#혹시 오류나면 else아니라     elif vid_status == 0 :으로

def show_vid(request):
    global vid_status
    if request.method == 'POST':
        img = request.FILES.get('img-file')
        Image.objects.create(img=img)
        #video_path패턴으로 설정
        video_path = "https://deept.s3.ap-northeast-2.amazonaws.com/usr/Kakao1.mp4"
        #결과값을 템플릿에 띄우는 법
        result = do(video_path)
        vid_status = 1
        return redirect(show_vid)

    elif vid_status == 1 :
        img = Image.objects.last()
        context = {
            'object': img
            }
        vid_status = 0
        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html')

def show_img(request):
    global img_status
    if request.method == 'POST':
        img = request.FILES.get('img-file')
        Image.objects.create(img=img)
        #패스
        #실행
        img_status = 1
        return redirect(show_img)
    
    elif img_status == 1 :
        img = Image.objects.last()
        context = {
            'object': img
            }
        img_status = 0
        return render(request,'image.html', context)

    else:
        return render(request,'image.html')