from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
import pymysql
from accounts.models import Account
from posts.models import Product


def blueprint(request):
    return render(request,'blueprint.html')

def index(request):
    """con=pymysql.connect(host="localhost",user="root",password="Ashu#@$2799",database="amazon")
    cur=con.cursor()
    cur.execute("select * from products")
    cursor=cur.fetchall()
    listt=[]
    for i in cursor:
        listt.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        print("appended")

    con.close()"""
    products=Product.objects.all()
    """listt=[]
    for i in products:
        print(i.image)
        listt.append((i.title,i.price,i.image,i.mrp,i.saving))
        print("appended")"""

    return render(request,'index.html',{'listt':products})

def search(request):
    if request.method=='GET':
        s=request.GET['search']
        allpro=Product.objects.all()
        sortpro=[]
        for pro in allpro:
            if s in pro.title.lower():
                sortpro.append(pro)
        if sortpro:
            return render(request,'search.html',{'sortpro':sortpro})
        else:
            return render(request,'search.html',{'notfound':"No Product found"})
