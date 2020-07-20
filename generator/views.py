from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 14)) # second argument is for default values
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepassword = ''
    thepassword2 = ''
    for x in range(length):
        thepassword += random.choice(characters)
        thepassword2 += random.choice(characters)
    
    return render(request, 'generator/password.html',{'password': thepassword, 'password2':thepassword2})

def about(request):
    return render(request, 'generator/about.html')