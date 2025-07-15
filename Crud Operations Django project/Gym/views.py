from django.shortcuts import render, redirect
from Gym.models import Gymdata
from django.views.decorators.csrf import csrf_exempt

# Home page view
@csrf_exempt
def Gym1(request):
    return render(request, 'Gympage1.html')


# Services page
def service_view(request):
    return render(request, 'gym_services.html')  

# About page
def gym_about(request):
    return render(request, 'gym_about.html')

# Better: use this as the new contact view if you want cleaner naming
@csrf_exempt
def gym_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(f"Received from form: {name} | {email} | {message}")  # Debug print

        Gymdata.objects.create(name=name, email=email, message=message)
        return render(request, 'Gympage2.html', {'name': name})
    
    return render(request, 'gym_contact.html')
