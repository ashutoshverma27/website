from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import pymysql
from django.db import connection
from .forms import details
import requests
from bs4 import BeautifulSoup
import re


def blueprint(request):
    return render(request,'blueprint.html')
def index(request):
    print("hlsaflksladjfkhaskfhlkasfh")
    con=pymysql.connect(host="localhost",user="root",password="Ashu#@$2799",database="amazon")
    cur=con.cursor()
    cur.execute("select * from products")
    cursor=cur.fetchall()
    print(cursor)
    listt=[]
    for i in cursor:
        listt.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        print("appended")
    con.close()


    post=request.GET.get('post','')
    fullname=request.GET.get('fullname','')
    email=request.GET.get('email','')
    return render(request,'index.html',{'post':post,'listt':listt})
def add(request):
    return render(request,'add.html')

def added(request):
    con=pymysql.connect(host="localhost",user="root",password="Ashu#@$2799",database="amazon")
    cur=con.cursor()
    url= request.GET['link']
    print(url)

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html5lib')

    title=soup.find('span', {'class' : 'a-size-large'})
    price=soup.find('span', {'class' : 'a-size-medium a-color-price priceBlockBuyingPriceString'})
    image=soup.find('img', {'id' : 'landingImage'})
    mrp=soup.find('span', {'class' : 'priceBlockStrikePriceString a-text-strike'}).get_text()
    saving=soup.find('td', {'class' : 'a-span12 a-color-price a-size-base priceBlockSavingsString'})
    print(title.get_text(),price.get_text(),image['data-old-hires'],mrp,saving)

    sql="""INSERT INTO products(title,url,image, price,mrp,saving) \
             VALUES (%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql,(title.get_text(),url,image['src'],price.get_text(),mrp,saving.get_text()))
    con.commit()
    con.close()
    error="added successfuly"



    return   render(request,'add.html',{'error':error})



def index1(request):
    return render(request,'index1.html')

def blog(request):


    posts=request.GET.get('post','')

    #database created
    #cur.execute('create Database blog')
    #table created named blog
    #cur.execute('create table blog(post text(1000))')
    with connection.cursor() as cur:
        sql="""insert into blog(post) values(%s)"""
        cur.execute(sql,(posts))
        con.commit()
        cur.execute("select * from blog")
        ff=cur.fetchall()
    lis=[]
    for i in ff:
        lis.append(i)
        print('blog created')
    return render(request,'blog.html',{'lis':lis})
    cur.close()
@csrf_exempt
def login(request):
        if request.method=='POST':
            form=details(request.POST)
            if form.is_valid():
                print("True")
            return render(request,'login.html',{'form':form})




def signup(request):
    return render(request,'signup.html')
    """ fullname=request.GET.get('fullname','')
         username=request.GET.get('username','')
         email=request.GET.get('email','')
         password=request.GET.get('password','')

         with connection.cursor() as cur:

             sql="INSERT INTO user(fullname,username, email, password)
                 VALUES (%s,%s,%s,%s)""

             cur.execute(sql,(fullname, username, email,password))

             print("added")"""



def loggedin(request):
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        with connection.cursor() as db:

            sql="select * from user where email=%s and password=%s"
            db.execute(sql,(email,password))
            result = db.fetchone()
            print(result)

        if result==None:
            return render(request,'login.html')
            print("email does not exists")



        else:
               print("You are Welcome",result[0])
               print("Now you are logged in!!")
               confirm="Now you are logged in!!"
               account=[]
               for i in result:
                   account.append(i)

               return render(request,'loggedin.html',{'account':account,'confirm':confirm})
