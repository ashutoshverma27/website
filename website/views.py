from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pymysql
from django.db import connection
from .forms import details



def blueprint(request):
    return render(request,'blueprint.html')
def index(request):
    post=request.GET.get('post','')
    fullname=request.GET.get('fullname','')
    email=request.GET.get('email','')
    return render(request,'index.html',{'post':post})


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
