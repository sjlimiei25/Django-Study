from django.shortcuts import render, redirect

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
    name = request.POST.get('name')
    price = request.POST.get('price')
    stock = request.POST.get('stock')
    desc = request.POST.get('desc')

    # DB에 저장(추가)
    Product.objects.create(name=name, price=price, stock=stock, desc=desc)

    # 목록페이지로 이동
    return redirect('funcview:index')
    
def detail_product(request):
  # 요청 시 전달된 데이터 추출
  #  - 요청 방식 : GET
  id = request.GET.get('id')

  # 해당 값으로 조회
  product = Product.objects.get(id=id)

  return render(request, 'funcview/detail_product.html', {'product': product})