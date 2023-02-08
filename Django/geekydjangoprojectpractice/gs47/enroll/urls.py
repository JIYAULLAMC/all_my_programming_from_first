from django.urls import path
from . import views


urlpatterns = [
    path("regi/",views.register, name="register"),
]