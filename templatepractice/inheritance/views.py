from django.shortcuts import render

# Create your views here.

# http://.../inherit/
def index(request):
  return render(request, 'inheritance/index.html')

# http://.../inherit/sub/
def sub(request):
  return render(request, 'inheritance/sub.html')