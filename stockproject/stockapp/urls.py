from django.urls import path
from . import views

app_name = 'stockapp'

urlpatterns = [
  path('stock/', views.scrape_stock_by_name, name='stock_search')
]