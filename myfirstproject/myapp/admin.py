from django.contrib import admin
from myapp.models import Post

# Register your models here.
# 관리자 사이트에서 관리하기 위한 모델 설정

# Post 모델(테이블)을 관리하기 위해 등록
admin.site.register(Post)