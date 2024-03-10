from django.shortcuts import render,redirect
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request,"home.html",context)

def loginn(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        
        userr=authenticate(username=uname,password=password)
        if userr is not None:
            login(request,userr)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request,"loginn.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        newuser=User.objects.create_user(username=username,email=email,password=password )
        newuser.save()
        return redirect("/login")
    return render(request,"signup.html")

def newpost(request):
    if request.method=='POST':
        title=request.POST.get("utitle")
        content=request.POST.get("ucontent")
        npost=Posts(title=title,content=content,author=request.User)
        npost.save()
        return redirect('/home')
    return render(request,"newpost.html")



def mypost(request):
    context = {
        'posts': Posts.objects.filter(author= request.user)
    }
    return render(request, 'mypost.html', context)
