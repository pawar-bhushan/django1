from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
un=''
pwd=''
# Create your views here.
def loginaction(request):
    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", password=" ", database='userdata', table='users')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                un=value
            if key=="password":
                pwd=value
        c="select * from users where username='{}' and password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return HttpResponse("Please check the values")
        else:
            return HttpResponse("Welcome" + un)
    return render(request,'login.html')