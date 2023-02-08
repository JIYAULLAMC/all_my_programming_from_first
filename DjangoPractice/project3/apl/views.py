from django.http import HttpResponse
from django.shortcuts import render
from apl.models import conn, plat

# Create your views here.


def home(request):
    return HttpResponse(' <h1> Home page </h1>')



def showdatabases(request):
    query = 'show databases'
    plat.execute(query)
    res = plat
    return HttpResponse(res)


def usedatabase(request, name):
    query = f'use {name}'
    plat.execute(query)
    res = plat
    return HttpResponse('database is under exicution')


def showtables(request):
    query = 'show tables'
    plat.execute(query)
    res = plat.fetchall()
    print(res)    
    return HttpResponse(f'all tables are {res}')

def createtable(request):
    query = 'create table bottle( id int primary key, name varchar(20)) '
    plat.execute(query)
    conn.commit()
    return HttpResponse(f'the table is created ')
     

def insert(request,id,name):
    val = [id,name]
    query = 'insert into bottle (values(%d,%s))'
    plat.execute(query)
    res = plat.fetchall()
    conn.commit()
    return HttpResponse('record is created', res)

