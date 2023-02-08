from app1 import views
from django.urls import path

app_name = 'app1'

urlpatterns = [
    path('app1home/', views.app1home, name='app1home'),
    path('app1about/', views.app1about, name='app1about'),
]