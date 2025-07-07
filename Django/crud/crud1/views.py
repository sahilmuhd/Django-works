from django.shortcuts import render
from django.http import HttpResponse
from crud1.models import Contacts
# Create your views here.

def index(request):
    contacts = Contacts.objects.all()
    return render(request,'table.html',{'data': contacts})

def index2(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('number')
    address = request.POST.get('address')
    
    contact = Contacts(name=name, email=email, number=number, address=address)
    contact.save()
    
    return render(request, 'table.html', {'data': Contacts.objects.all()})
