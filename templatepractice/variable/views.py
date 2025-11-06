from django.shortcuts import render
import datetime

# Create your views here.

def index(request):

  context = {
    'name': '아이유(Iu)',
    'age': 33,
    'songs': ['좋은날', '미아', '밤편지'],
    'introduce': '<b>노래 좋아요!</b>', 
    'today': datetime.datetime.now(),
    'pi': 3.141592
  }

  return render(request, 'variable/variable.html', context)