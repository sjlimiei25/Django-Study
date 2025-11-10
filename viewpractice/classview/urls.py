from django.urls import path
from .views import IndexView, NewView

app_name = 'classview'

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('new/', NewView.as_view(), name='new'),
]