from django.shortcuts import render
from django.http import HttpResponse
from crud1.models import Contactdata
# Create your views here.
def crud(request):
    queryset=Contactdata.objects.all()
    return render(request,'crud.html',{'data':queryset})
def contactentry(request):
    queryset=Contactdata.objects.all()
    name=request.POST.get('txtName','no-name') or 'no-name'
    email=request.POST.get('txtEmail','no-email') or 'no-email'
    mobile=request.POST.get('txtMobile','no-mobile') or 'no-mobile'
    #print(name+" "+email+" "+mobile)
    contact=Contactdata(name=name,email=email,mobile=mobile)
    contact.save()
    return render(request,'crud.html',{'data':queryset})
def deletecontact(request,id):
    deleterec=Contactdata.objects.get(id=id)
    deleterec.delete()
    queryset=Contactdata.objects.all()
    return render(request,'crud.html',{'data':queryset})
def editcontact(request,id):
    queryset=Contactdata.objects.get(id=id)
    return render(request,'edit.html',{'data':queryset})
def updatecontact(request):
    name=request.POST.get('txtName','no-name') or 'no-name'
    email=request.POST.get('txtEmail','no-email') or 'no-email'
    mobile=request.POST.get('txtMobile','no-mobile') or 'no-mobile'
    id=request.POST.get('txtId','no-mobile') or 'no-mobile'
    Contactdata.objects.filter(id=id).update(name=name,email=email,mobile=mobile)
    queryset=Contactdata.objects.all()
    return render(request,'crud.html',{'data':queryset})
