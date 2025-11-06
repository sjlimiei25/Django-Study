from django.urls import path
from . import views

# 템플릿 태그 중 url 태그가 앱 이름으로 찾을 수 있도록 설정
app_name = 'tag'

# 기본 요청 주소 : http://.../tag/
urlpatterns = [
    path('', views.index, name='index'),
    path('if/', views.if_tag, name='if'),
    path('for/', views.for_tag, name='for'),
    path('static/', views.static_tag, name='static'),
]
