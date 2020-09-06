from django.db import models
#2. 모델 만들기
# Create your models here.

#$python manage.py makemigrations 와
#$python manage.py migrate로 디비에 모델을 적용 시켜준다

class Image(models.Model):
    objects = models.Manager()
    img = models.FileField(upload_to='usr')

#미디어 파일이 usr 라는 폴더 안에 들어가 있는 것을 볼 수 있는데 이는 모델에서 img 필드를 생성할 때 지정한 upload_to 옵션 때문이다.