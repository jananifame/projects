from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')
def password(request):

    char=list('abcdefghijklmnopqrstuvwxyz')
    length= int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        char.extend(list('1234567890'))
    if request.GET.get('special characters'):
        char.extend(list('!@#$%^&*()_+":<>?"'))
    thepassword=''
    for i in range(length):
        thepassword += random.choice(char)

    return render(request,'generator/password.html',{'password':thepassword})
def about(request):
    return render(request,'generator/about.html')
