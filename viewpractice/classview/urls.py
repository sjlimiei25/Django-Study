from django.urls import path
from .views import IndexView, NewView, ProductDetailView

app_name = 'classview'

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('new/', NewView.as_view(), name='new'),
  path('detail/<int:id>/', ProductDetailView.as_view(), name='detail'),
]