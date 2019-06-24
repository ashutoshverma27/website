from django.http import HttpResponse
from django.shortcuts import render
import pymysql


def home(request):
    return render(request,'home.html')
def index(request):
    post=request.GET.get('post','')
    fullname=request.GET.get('fullname','')
    email=request.GET.get('email','')


    con=pymysql.connect(host='localhost',user='root',password='Ashu#@$2799',database='blogs')
    cur=con.cursor()
    #database created
    #cur.execute("create database blogs")
    try:
        sql='''insert into %s(id,post) values(%s)'''
        cur.execute(sql,(email))
        cur.commit()
        print("tried")
    except:
        sql="""create table %s(id INT AUTO_INCREMENT PRIMARY KEY,\
         ,post char(255))"""
        cur.execute(sql,(email,post))
        print("excepted")
    finally:
        cur.close()




    return render(request,'index.html',{'post':post})
