from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def logindata(request):
    name=request.POST['email']
    pass1=request.POST['pass']
    print(name+" "+pass1)
    return HttpResponse('logindata')



def registerdata(request):
    name=request.POST['name']
    email=request.POST['email']
    number=request.POST['number']
    password=request.POST['password']
    print(name+email+number+password)
    return HttpResponse('registerdata')


# Create your views here.

def sub1(request):
    return render(request,'page1.html')


def sub2(request):
    name=request.POST['name']
    request.session['customername']=name
    return render(request,'page2.html')


def sub3(request):
    
    email=request.POST['email']
    request.session['customeremail']=email
    return render(request,'page3.html')
  
def sub4(request):
    number=request.POST['number']
    print(request.session.get('customername')+" "+request.session.get('customeremail'))
    return render(request,'page4.html')

def list1(request):
    #skills=request.POST.get('skills')
    request.session['skills']
    return render(request,'list.html')

def list2(request):
    skills=request.POST['skills']
    request.session['skills']=skills
    print(request.session.get('skills'))
    return render(request,'listcollected.html')





  











