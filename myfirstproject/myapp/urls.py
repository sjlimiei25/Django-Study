from django.urls import path
from . import views


# http://.../myapp/...
urlpatterns = [
  path('', views.post_list, name='post_list'),  # 요청주소 : http://.../myapp/
  path('new/', views.new_post, name='new_post'), # 요청주소 : http://.../myapp/new/
]

# path(route, view, name)
# - route : URL 패턴 문자열
# - view  : URL과 매칭되어 호출되는 뷰 함수(처리할 함수)
# - name  : 각 URL 패턴별 이름
