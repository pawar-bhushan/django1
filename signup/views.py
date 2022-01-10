from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
dob=''
un=''
pwd=''
s_ans=''
adds=''
# Create your views here.
def signaction(request):
    global fn, ln, dob, un,pwd, s_ans, adds
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", password=" ", database='userdata', table='users')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="dob":
                dob=value
            if key=="username":
                un=value
            if key=="password":
                pwd=value
            if key=="sanswer":
                s_ans=value
            if key=="address":
                adds=value
        
        c="insert into users values('{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,dob,un,pwd,s_ans,adds)
        cursor.execute(c)
        m.commit()
    return render(request,'signup.html')