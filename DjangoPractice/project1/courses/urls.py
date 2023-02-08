from django import views
from django.urls import path

from courses import views


urlpatterns = [
    path('courses/',views.courses, name='courses')
]