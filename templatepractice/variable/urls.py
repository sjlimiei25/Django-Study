from django.urls import path
from . import views

# 템플릿 태그 중 url 태그가 앱 이름으로 찾을 수 있도록 설정
app_name = 'variable'

# 기본 요청 주소 : http://.../variable/
urlpatterns = [
    path('', views.index, name='index')    
]
