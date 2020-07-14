from django.shortcuts import render
import random


def home(request):
    return render(request, 'html/home.html')

def about(request):
    return render(request,'html/about.html')

def password(request):
    yourPassword = ""

    characters = list('abcdefghijklmnopqrstuvxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#%^$&*()_+?/'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length'))
    for x in range(length):
        yourPassword += random.choice(characters)

    context = {'password':yourPassword}
    return render(request, 'html/password.html', context)
