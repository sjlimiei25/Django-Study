# scrapping_practice.py
"""
    웹 스크래핑 (Web Scrapping)
    : 특정 웹 페이지에서 필요한 데이터 부분을 스크랩하는 작업
      HTML 요소에서 원하는 정보만 가져옴
      예) 뉴스 제목, 제품 가격, 종목 정보 등등

    웹 크롤링 (Web Crawling)
    : 특정 웹 페이지 전체를 복제하는 작업
      보통 검색 엔진에서 사용
      예) 사이트 전체 페이지 다운로드, 링크 이동과 함께 데이터 수집
"""

# 1) 필요한 라이브러리(패키지) 설치 : pip install 라이브러리명
#    requests, beautifulsoup4

import requests # 웹 페이지 내용을 가져오는 라이브러리 (HTML, JSON, 파일 등)
from bs4 import BeautifulSoup # HTML을 파싱하고 필요한 데이터를 추출 (선택자를 통해 원하는 정보를 추출)


# 2) 명언 사이트 스크랩
url = 'https://quotes.toscrape.com/'
# -> 스크랩할 웹 페이지 주소

# 웹 페이지에 요청 후 응답 정보를 저장
response = requests.get(url)

# print(response) # <Response [200]> => 요청 성공 시 출력 내용
# print(response.text) # 해당 웹 페이지의 HTML 정보 확인

# HTML 파싱 (분석)
soup = BeautifulSoup(response.text, 'html.parser')

# 필요한 데이터 추출
quotes = soup.select('div.quote span.text') # 명언 내용 부분을 추출

# print(quotes)

# 명언 목록 출력
"""
for q in quotes:
  #print(q)
  text = q.get_text()
  print(text)
"""

# 사용자로부터 입력받은 키워드에 해당하는 명언만 출력
keyword = input('키워드를 입력하세요 : ')
for q in quotes:
  if keyword.upper() in q.get_text().upper():    # 특정문자열 in 전체문자열 : 전체 문자열안에 특정 문자열이 포함되어 있다면 True, 그렇지않으면 False
    print(q.get_text())

"""
    * 스크래핑(크롤링) 시 주의사항 *

    1) 사이트 정책 확인 : robots.txt 및 이용약관 확인
        대규모 요청 또는 상업적 사용이 허용되지 않는 경우 주의
    2) 요청 간격 조절 : 서버 과부하 방지 (time.sleep 등을 사용하여 지연 요청)
    3) User-Agent 설정 : requests 시 headers 지정
        일부 사이트에서는 해당 설정이 필요할 수 있음. 웹 브라우저 정보를 작성
    4) 개인정보 주의 : 로그인/민감 정보 무단 수집 금지
    5) 웹 구조 변경 가능 : 해당 사이트 HTML/CSS가 변경될 경우 코드 오류 발생 가능. 오류 발생 시 파악 후 대응 필요.
"""

## TODO: 스터디 과제 ##
#  입력된 키워드에 해당하는 명언을 총 5개 출력해보자.
#  1) 사이트 분석 -> 페이지 이동 발생할 수 있음...
#  2) 분석을 바탕으로 코드 작성

# 작성한 코드를 이메일로 제출 (~ 12:40까지)
# 제목: 251112 스크래핑 그룹 과제 (X팀)
# 참조: 팀원 이메일, 팀원 이메일, ...