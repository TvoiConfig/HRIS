from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...


def register(request):
    if request.method =="POST":
        form = UserOurRegistration(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserOurRegistration()
    return render(request, 'users/reg.html', {'form': form})

