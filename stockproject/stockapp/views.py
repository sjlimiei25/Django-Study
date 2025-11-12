from django.shortcuts import render
from django.http import JsonResponse

import requests
from bs4 import BeautifulSoup

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

  # 네이버 증권 페이지, 스크래핑
  request_url = f'https://finance.naver.com/search/search.naver?query={name}&endUrl='

  print(f'요청 URL -----> {request_url}')

  response = requests.get(request_url)
  # response.text

  soup = BeautifulSoup(response.text, 'html.parser')

  # 종목명으로 검색한 항목들 중 첫번째 항목만 선택
  first_element = soup.select_one('td.tit a')
  # select_one : CSS 선택자를 사용하여 조건에 맞는 첫 번째 HTML 태그 추출. 없으면 None.

  # 검색 결과가 없을 경우, "해당 종목이 존재하지 않습니다." JSON 데이터를 리턴(응답)
  if not first_element:
    return JsonResponse({"error": "해당 종목이 존재하지 않습니다."})
  
  # -- 검색 결과가 있는 경우 --
  # first_element => <a href="...?code=xxxx">종목명...
  first_ele_href = first_element['href']     # => '...?code=xxxx'
  tokens = first_ele_href.split("code=")  # => ['...?', 'xxxx']
  code = tokens[-1] # => 'xxx' 종목에 대한 코드값
  # code = first_element['href'].split("code=")[-1]

  # 상세 정보 스크래핑
  detail_url = f'https://finance.naver.com/item/main.naver?code={code}'

  res = requests.get(detail_url)  # 요청
  soup = BeautifulSoup(res.text, 'html.parser')

  # 현재가 : p.no_today span
  today_prices = soup.select('p.no_today span')
  t_price = ''
  for value in today_prices:      # ['1', '2', .., '8', '0']
    t_price += value.text.strip()  

  # 시가총액 : em#_market_sum
  market_sum = soup.select_one('em#_market_sum').text.strip()
  # 문자열.strip() : 공백, 줄바꿈을 제거

  # 종목명(풀네임) : div.h_company h2 a
  full_name = soup.select_one("div.h_company h2 a").text.strip()

  data = {
    "name": full_name,        # 종목명
    "code": code,             # 종목코드
    "price": t_price,         # 현재가
    "market_sum": market_sum  # 시가총액
  }

  return JsonResponse(data)