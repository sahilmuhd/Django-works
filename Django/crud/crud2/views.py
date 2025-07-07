from django.shortcuts import render
from django.http import HttpResponse
from crud2.models import employee


# Create your views here.

def first(request):
    return render(request,'details.html')

def second(request):
    name = request.POST['name']
    email = request.POST['email']
    address = request.POST['address']
    number = request.POST['number']
    print(name,email,address,number)
    employee.objects.create(name=name, email=email , address=address, number=number)
    data = employee.objects.all()
    return render(request,'details2.html',{'data':data})






