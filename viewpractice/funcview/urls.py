from django.urls import path
from . import views

app_name = 'funcview'

# 기본 요청 주소 : http://.../fv/
urlpatterns = [
  path('', views.index, name='index'),
  path('new/', views.new_product, name='new_product'),
  path('detail/', views.detail_product, name='detail')
]