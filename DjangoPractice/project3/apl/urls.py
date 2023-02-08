from django.urls import path
from apl import views
urlpatterns = [
    path('home/',views.home, name='home' ),
    path('showdatabases/',views.showdatabases, name='showdatabases' ),
    path('usedatabase/<name>',views.usedatabase, name='usedatabase' ),
    path('showtables/',views.showtables, name='showtables' ),
    path('createtable/',views.createtable, name='createtable' ),
    path('insert/<id>/<name>',views.insert, name='insert' ),

]