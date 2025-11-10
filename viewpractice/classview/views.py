from django.shortcuts import render
from django.views import View

from .models import Product

# Create your views here.

# 클래스형 뷰
class IndexView(View):
  def get(self, request):
    list = Product.objects.all()
    return render(request, 'classview/index.html', {'list': list})
  
class NewView(View):
  def get(self, request):
    return render(request, 'classview/new_product.html')