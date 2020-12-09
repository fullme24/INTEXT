from django import forms
from django.shortcuts import render, redirect
from . import views, models
from .models import Person


def session(request):
    username = None
    if request == 'GET' :
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return render(request, 'homepage/index.html')
            if 'username' in request.session:
                username = request.session['username']
        elif request.method == 'POST':
            form_login = FormLogin(request.POST)
            if form_login.is_valid():
                username = form_login.cleaned_data['username']
                password = form_login.cleaned_data['password']
                try:
                    data = Person.objects.get(user_name=username, password=password)
                    request.session['username'] = username
                except:
                    username = None
        return render(request, 'login/logged_in.html', { 'form':form_login, 'username': username})
