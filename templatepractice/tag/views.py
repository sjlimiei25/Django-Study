from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'tag/index.html')

def if_tag(request):
  context = {
    'user': {
      'name': '스폰지밥',
      'age': 13,
      'is_admin': False
    }
  }
  return render(request, 'tag/if_tag.html', context)

def for_tag(request):
  context = {
    'menu_list': [
      {'name': '아이스 아메리카노', 'price': 1600, 'is_soldout': False},
      {'name': '민트초코라떼', 'price': 3800, 'is_soldout': False},
      {'name': '캐모마일티', 'price': 2300, 'is_soldout': True},
    ]
  }
  return render(request, 'tag/for_tag.html', context)

def static_tag(request):
  context = {
    'image_url': 'tag/images/flower.jpg'
  }
  return render(request, 'tag/static_tag.html', context)