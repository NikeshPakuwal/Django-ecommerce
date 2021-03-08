from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# store view
def store(request):
    context = {}
    return render(request, 'store/store.html', context)

#cart view
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

#base html
@login_required(login_url='login')
def adminHome(request):
    context = {}
    return render(request, 'admin/dashboard/home.html')
