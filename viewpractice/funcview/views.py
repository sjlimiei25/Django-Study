from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
  data = Product.objects.all()
  return render(request, 'funcview/index.html', {'list': data})