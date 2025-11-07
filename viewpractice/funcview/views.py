from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
  data = Product.objects.all()
  return render(request, 'funcview/index.html', {'list': data})

def new_product(request):
  if request.method == 'GET':
    return render(request, 'funcview/new_product.html')
  elif request.method == 'POST':
    # 요청 시 전달된 데이터 추출
    # DB에 저장(추가)
    # 목록페이지로 이동
    pass