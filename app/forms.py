
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
  
  
  
class UserRegisterForm(UserCreationForm): 
    user_name = forms.CharField(max_length = 20) 
    password = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'password'] 
