from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from crud1.models import Contacts
# Create your views here.

def index(request):
    contacts = Contacts.objects.all()
    return render(request,'table.html',{'data': contacts})

def index2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')

        # Optional: Basic validation
        if not all([name, email, number, address]):
            return HttpResponseBadRequest("All fields are required")

        Contacts.objects.create(name=name, email=email, number=number, address=address)
        return redirect('index')  # Redirect to prevent form re-submission on refresh
    else:
        return HttpResponseBadRequest("Invalid request method")