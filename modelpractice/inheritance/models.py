from django.db import models

# Create your models here.
"""
# -- 상속 적용 전 모델 정의 --
class Deposit(models.Model):
  name = models.CharField(max_length=100)
  bank_name = models.CharField(max_length=50)
  interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
  create_date = models.DateField()
  period_month = models.IntegerField()
  min_balance = models.IntegerField()

  def __str__(self):
    return f'{self.name} / {self.bank_name}'
# --------------------
class Loan(models.Model):
  name = models.CharField(max_length=100)
  bank_name = models.CharField(max_length=50)
  interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
  create_date = models.DateField()
  limit_amount = models.IntegerField()
  credit_point = models.IntegerField()

  def __str__(self):
    return f'{self.name} / {self.bank_name}'
"""
# -- 상속 적용 후 모델 정의 --
class Product(models.Model):
  # 현재 모델은 테이블로 생성하지 않고, 상속 용도로만 사용하고자 할 경우
  class Meta:
    abstract = True

  name = models.CharField(max_length=100)
  bank_name = models.CharField(max_length=50)
  interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
  create_date = models.DateField(auto_now_add=True)  

  def __str__(self):
    return f'{self.name} / {self.bank_name}'
  

class Deposit(Product):
  period_month = models.IntegerField()
  min_balance = models.IntegerField()
  
# --------------------
class Loan(Product):
  limit_amount = models.IntegerField()
  credit_point = models.IntegerField()
