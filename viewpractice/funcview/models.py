from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=30)
  price = models.IntegerField()
  stock = models.IntegerField()
  desc = models.TextField()

  def __str__(self):
    return f'{self.name} / {self.price} / {self.stock} / {self.desc}'