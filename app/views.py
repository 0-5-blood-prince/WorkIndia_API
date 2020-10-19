from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm 
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from django.http import HttpResponse
# Create your views here.
def register(request):
    print(request)
    if request.method == "POST":
    	form = UserRegisterForm(request.POST)
    	if form.is_valid():
    		form.save()
    		username = form.cleaned_data.get('username')
    		password = form.cleaned_data.get('password')
    		messages.success('Your account has been created ! You are now able to log in')
    		return HttpResponse("Account Created")
    return HttpResponse("Sorry")

def Login(request):
	return None




# user = User.objects.create{
			#      name = name,
			#      password = password
			# }