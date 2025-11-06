# readme.md

## 프로젝트 생성
> django-admin startproject 프로젝트명

## 개발 서버 실행 (프로젝트 실행)
> python manage.py runserver

## 기본 테이블 생성 / 데이터베이스 변경 사항 반영
> python manage.py migrate

## 마이그레이션 파일 생성
> python manage.py makemigrations [앱이름]

## 관리자 계정 생성 (슈퍼유저)
> python manage.py createsuperuser
> admin / 1q2w3e4r5%Z


## 새 앱 생성
> python manage.py startapp 앱이름
1. 앱 생성 명령어 작성
2. 설정 폴더(myfirstproject/)의 settings.py 파일에
   INSTALLED_APPS 옵션에 추가한 앱 이름 설정
3. 모델 정의 : 새 앱 폴더(myapp/)의 models.py
4. 마이그레이션 파일 생성 -> makemigrations 명령어 실행
5. 데이터베이스 반영 -> migrate 명령어 실행
6. 관리자 페이지에 모델 등록 : 앱 폴더(myapp/)의 admin.py (선택)
7. 비즈니스 처리 로직 추가 : 앱 폴더(myapp/)의 views.py
8. 템플릿 파일 추가 
   - 기본      : 앱 폴더(myapp/) / templates / 앱폴더(myapp/) / 템플릿_파일명
   - 전역 설정 : 설정 파일(settings.py) 기준. BASE_DIR / templates / 앱폴더(myapp/) / 템플릿_파일명
9. URL 매핑 처리 : 앱 폴더(myapp/) 의 urls.py , 설정폴더(myfirstproject) 의 urls.py