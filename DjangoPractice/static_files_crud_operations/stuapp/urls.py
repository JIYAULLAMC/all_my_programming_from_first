from django.urls import path
from stuapp import views
urlpatterns = [
    path("sboot/",views.sboot, name="sboot"),
    path("shome/",views.shome, name="shome"),
    path("slist/",views.slist, name="slist"),
    path("studata/<int:pk>/",views.studata, name="studata"),
    path("screate/",views.screate, name="screate"),
    path("supdate/<int:pk>/",views.supdate, name="supdate"),
]