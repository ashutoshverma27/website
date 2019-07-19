from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account
from django.utils import timezone
from posts.models import Product
def home(request):
    return render(request,'accounts/home.html')

def login(request):
     return render(request,'accounts/login.html')

def signup(request):
    if request.method=='POST':
        if request.POST['fullname'] and request.POST['username'] and request.POST['password']:
            account=Account()
            account.fullname=request.POST['fullname']
            account.username=request.POST['username']
            account.password=request.POST['password']
            account.date=timezone.datetime.now()
            account.save()
            return render(request,'accounts/login.html',{'msg':'You are successfully signed up.Login Here'})
        else:
            return render(request,'accounts/signup.html',{'error':'Fields can not be empty.'})

    return render(request,'accounts/signup.html')



def loggedin(request):
    if request.method=='POST':
        if request.POST['username'] and request.POST['password']:
            users=Account.objects.all()
            #email=request.POST.get('email','')
            #password=request.POST.get('password','')
            for user in users:
                if user.username==request.POST['username'] and user.password==request.POST['password']:
                    fname=user.fullname
                    request.session['username']=user.username
                    request.session['fname']=user.fullname
                    print(user.fullname)
                    return redirect('index')
            else:
                return render(request,'accounts/login.html',{'msg':'User does not exist!'})


    else:
          return redirect('index')

def logout(request):
    request.session.clear()
    msg='Hey,You are logged out'
    return render(request,'accounts/login.html',{'msg':msg})

def profile(request):
    if 'username' in request.session:
        #improved code
        user=Account.objects.get(username=request.session['username'])
        ##yeh code pahle likha tha
        """for user in users:
            if user.username==request.session['username']:
                fname=user.fullname
                uname=user.username
                date=user.date
                userdata={'fname':fname,'uname':uname,'date':date}"""
        ###################################################################
        return render(request,'accounts/profile/profile.html',{'user':user})

    else:
        return render(request,'accounts/login.html',{'msg':'Login to view your profile!'})

def reset_pass(request):
    if request.method=="POST":
        if request.POST['password1']==request.POST['password2']:
            if 'username' in request.session:
                print(request.session['username'])
                user=Account.objects.get(username=request.session['username'])
                user.password=request.POST['password1']
                user.save()
                request.session.clear()
            user=Account()

            return render(request,'accounts/login.html',{'msg':'Login again for security purpose'})
        else:
            print("else statement")
            return render(request,'accounts/profile/reset_pass.html',{'error':'Password does not match!'})
    else:
        print("outer else")
        return render(request,'accounts/profile/reset_pass.html')
def cart(request):
    if 'username' in request.session:
        user=Account.objects.get(username=request.session['username'])
        return render(request,'accounts/profile/cart.html',{'user':user})
    else:
        return render(request,'accounts/login.html',{'msg':'login to view your cart'})
def addtocart(request):
    if request.method=='GET':
        product_url=request.GET.get('{{i.title}}','')
        #pro=Product.objects.get(title=product_url)
        #print(pro)
        print("lfkjsakljf",product_url)
        products=Product.objects.all()
        return render(request,'index.html',{'message':'Added to Cart','listt':products})
