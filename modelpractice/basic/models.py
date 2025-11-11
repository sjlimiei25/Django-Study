from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  # email = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  join_date = models.DateField()
  # is_active = models.IntegerField()
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.name} / {self.age} / {self.email}'