from django.shortcuts import render, redirect 
from .forms import NewUserForm 
from django.contrib.auth import authenticate, login as dj_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
  if request.method == 'POST':
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      messages.success(request,'Accounts Added successfully ')
    else:
      messages.error(request, 'unsuccessful registration')
  form = NewUserForm
  
  return render(request,'accounts/register.html',{'form':form})




def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
        dj_login(request, user)
        messages.info(request,f"welcome {username}")
        return redirect('products:home')
      else:
        messages.error(request,'invalid username or password')
    else:
      messages.error(request,'invalid username or password')
  form = AuthenticationForm()
  return render(request,'accounts/login.html',{'form':form})
    