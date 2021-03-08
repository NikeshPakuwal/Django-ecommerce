from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import auth
from .forms import AuthUser

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import (get_object_or_404,  render, HttpResponseRedirect) 

#registration page
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
    else:
        form = RegisterForm()
    return render(response, "admin/authentication/registration.html", {"form":form})

@login_required(login_url='login')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        #print(username)
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
    
    return render(request, 'admin/login.html')




#admin panel control view
def AdminUserList(request):
    data =  User.objects.all()
    return render(request, "admin/authentication/user_list.html", {'data' : data})

#user edit
def AdminUser(request, id):
    obj = get_object_or_404(User, id = id)

    form = AuthUser(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/auth/user')

    return render(request, 'admin/authentication/user_view.html', {'form' : form})

#user ajax delete
def user_delete(request):
    id = request.POST.get('id')
    news = User.objects.get(pk = id)
    news.delete()
    return JsonResponse({'success' : 'true'})
