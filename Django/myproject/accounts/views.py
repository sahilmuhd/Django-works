from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') # Replace 'home' with your desired success URL
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


