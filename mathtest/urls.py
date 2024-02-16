from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='test'),
    path('result/', views.result_view, name='result'),
]