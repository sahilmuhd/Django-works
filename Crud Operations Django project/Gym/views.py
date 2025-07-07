from django.shortcuts import render, redirect
from Gym.models import Gymdata
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Gym1(request):
    return render(request, 'Gympage1.html')

@csrf_exempt
def Gym2(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Gymdata.objects.create(name=name, email=email, message=message)
        print(name+email+message)

        return render(request, 'Gympage2.html', {'name': name})
