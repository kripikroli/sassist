from django.contrib import auth
from pathlib import Path

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    if user.user_type == 1:
                        return redirect('crm:admin_dashboard_view')
                    if user.user_type == 3:
                        return redirect('partners:partner_dashboard_view')

        else:
            error_message = form.errors

    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):

    logout(request)
    return redirect('login_view')