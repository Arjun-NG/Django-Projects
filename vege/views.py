from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your viees here.
def home(request):
    return render(request,"home/index.html")

@login_required(login_url="/login/")
def receipes(request):
    if request.method == 'POST':
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        receipe.objects.create(
            receipe_image=receipe_image,
            receipe_description=receipe_description,
            receipe_name=receipe_name
        )


    queryset=receipe.objects.all()

    if request.GET.get('search'):
       queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))


    context={"receipes":queryset}
    return render(request,"home/receipes.html",context)


def delete_receipe(request,id):
    queryset=receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset=receipe.objects.get(id=id)
   
    if request.method == 'POST':
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        queryset.save()
        return redirect('receipes')

    
    context={"receipe":queryset}


    return render(request,"home/update.html",context)


def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login/')
        
        

        user=authenticate(username=username ,password =password)
        if user is None:
            messages.error(request,"Invalid Credentials")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipes/')
    return render(request,"home/login.html")
    
def logout_page(request):
    logout(request)
    return redirect('/login/')
def register(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('pass')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,"The username is already taken...")
            return redirect('/register/')

        user=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            username=username
        )

        
        user.set_password(password)
        user.save()
        messages.info(request,"The Accouont is created successfull")
        return redirect("register")

    return render(request,"home/register.html")