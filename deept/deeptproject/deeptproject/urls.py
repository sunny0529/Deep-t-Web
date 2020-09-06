#5. url 설계 하기 = 해당 url로 접근 시, views.py 에 있는 함수를 실행시키고, 그 함수가 html 파일을 띄워주는 원리
#url 은 자식 myproject 안에 urls.py에서 처리해줄 수 있음.

"""deeptproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
import deeptapp.views #함수를 실행시켜야 하기 때문에 myapp 에 있는 views 를 import 해줍니다.
from deeptapp.views import show_vid
from deeptapp.views import show_img

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    url('^$',show_vid,name='vid'),
    url('image/',show_img,name='img'),

]
    #path('',myapp.views.home, name = 'home'), #새로운 path를 추가해주는데,
    #'' 과 같은 상황에서 myapp 안에 views 안에 home 함수를 실행시켜라 라는 의미입니다.
    #여기서 '' 같은 상황이라는 것은 우리의 주소 뒤에 붙는 내용을 의미합니다.
    #예를 들어 http://127.0.1:8000/  라는 주소 뒤에 첫 번째 path 처럼 admin/ 붙여주면 admin page가 열리게 되고.
    #두 번째 path 처럼 아무것도 붙여주지 않으면 home 함수를 실행해서 home.html 이 열리게 됩니다.
