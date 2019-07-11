from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'accounts/home.html')
@csrf_exempt
def login(request):
        if request.method=='POST':
            form=details(request.POST)
            if form.is_valid():
                print("True")
            return render(request,'accounts/login.html',{'form':form})


def signup(request):
    return render(request,'accounts/signup.html')
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

               return render(request,'accounts/loggedin.html',{'account':account,'confirm':confirm})
