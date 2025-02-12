from django.shortcuts import render,redirect,get_object_or_404
import mysql.connector as sql
from django.contrib import messages

fn=''
ln=''
s=''
em=''
pwd=''



# Create your views here.
def signup(request):
    global fn,ln,s,em,pwd
    context={}
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="062987",database='cakefairy')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
        # messages.success(request,"User Registered Successfully! ")
        context['message']=f"User Registered Successfully! "
        return redirect('login')

    return render(request,'signup.html',context)


    

def login(request):
    global em,pwd
    context={}
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="062987",database='cakefairy')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            context['message']=f"User Not Registered! , Please register to login"
            return render(request,'login.html',context)
        else:
            context['message']=f"Hey , Welcome to The Cake Fairy! "
            return render(request,'index.html',context)
        # context['message']=f"Hey , Welcome to The Cake Fairy! "
        
    return render(request,'login.html',context)