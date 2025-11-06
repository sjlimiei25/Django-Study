from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  create_at = models.DateTimeField(auto_now_add=True)

  # 자바에서 toString과 같이 
  # 현재 클래스의 내용을 문자열로 표현할 때 사용되는 함수
  def __str__(self):
    return f"{self.title} / {self.content} / {self.create_at}"