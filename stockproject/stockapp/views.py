from django.shortcuts import render
from django.http import JsonResponse

from .services import stock_service

# Create your views here.

# /api/stock?name=종목명

# 네이버 증권 페이지에서 종목명으로 검색했을 때 요청 주소
# => https://finance.naver.com/search/search.naver?query=KODEX&endUrl=

def scrape_stock_by_name(request):
  # 요청데이터에서 키워드 추출 : name
  # 요청 방식: GET
  name = request.GET.get('name')

  print(f'request data ----> {name}')

  # -------- * --------
  # 분리한 스크래핑 부분에 대한 함수 호출
  data = stock_service.get_stock_data(name)

  print(data)

  return JsonResponse(data)