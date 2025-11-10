from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Product

# Create your views here.

# 클래스형 뷰
# 기본적인 구조로 작성
"""
class IndexView(View):
  def get(self, request):
    list = Product.objects.all()
    return render(request, 'classview/index.html', {'list': list})
  
class NewView(View):
  def get(self, request):
    return render(request, 'classview/new_product.html')
  
  def post(self, request):
    # 상품 추가 -> 요청할 때 상품 정보를 전달
    name = request.POST.get('name')
    price = request.POST.get('price')
    stock = request.POST.get('stock')
    desc = request.POST.get('desc')

    # DB에 데이터 추가
    Product.objects.create(name=name, price=price, stock=stock, desc=desc)

    # 목록 페이지로 이동(메인페이지)
    return redirect('classview:index')

# http://.../cv/detail/<id>
class ProductDetailView(View):
  def get(self, request, id):
    product = Product.objects.get(id=id)
    return render(request, 'classview/detail_product.html', {'product':product})
"""

# 제네릭뷰 적용
class IndexView(ListView):
  template_name = 'classview/index.html'
  model = Product
  context_object_name = 'list' # 조회된 결과 데이터의 이름(키) 변경(기본값:object_list)

class NewView(CreateView):
  template_name = 'classview/new_product.html'
  model = Product
  fields = ['name', 'price', 'stock', 'desc']
  success_url = reverse_lazy('classview:index')
  # reverse_lazy() : 페이지 이동 주소를 나중에 계산해주는 함수 (실제 실행될 때 계산)

class ProductDetailView(DetailView):
  template_name = 'classview/detail_product.html'
  model = Product
  pk_url_kwarg = 'id' # URL에서 pk 대신 다른 이름으로 사용할 경우 지정 (기본값: pk)
  # context_ojbect_name 기본값 'object'

"""
  제네릭 뷰 (Generic View)

  * CRUD 기능 별 필수 속성
  - ListView (목록 조회)
    : model 또는 queryset, template_name
  - DetailView (상세 조회)
    : model 또는 queryset, template_name

  - CreateView (생성)
    : model, fields, template_name, success_url

  - UpdateView (수정)
    : model, fields, template_name, success_url

  - DeleteView (삭제)
    : model, template_name, success_url


  * 주요 속성 
    - model : 해당 뷰에서 사용할 데이터베이스 모델
    - queryset : 모델 대신 직접 쿼리셋 지정 (조회 조건)
      ex) queryset = Product.objects.filter(stock__gt=0)
    - template_name : 랜더링 시 사용할 HTML 템플릿 경로
    - fields : 생성/수정 시 사용될 데이터(모델) 필드 목록
    - success_url : 작업 완료(성공) 후 이동할 URL (보통 reverse_lazy() 함께 사용)
"""
