from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Profile, UserCustom
from .forms import RegistrationForm, ProfileForm


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    ''' create new account '''
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login/')
    form = {'form': form}
    return render(request, 'accounts/html/registration.html', form)    
        

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST) 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    form = AuthenticationForm()      
    return render(request, 'accounts/html/login.html', {'form': form})


def profiles(request, user_name):
    ''' if url equals username user can add info about profile or change '''
    if user_name == request.user.username:
        user_info = UserCustom.objects.get(username=request.user.username)
        form = RegistrationForm(instance=user_info)

        profile_info = Profile.objects.get(profile=request.user)
        form_profile = ProfileForm(instance=profile_info)

        if request.method == 'POST':
            form = RegistrationForm(request.POST, instance=user_info)
            form_profile = ProfileForm(request.POST, instance=profile_info)

            if form.is_valid():
                form.save()

            if form_profile.is_valid():    
                form_profile.save()      
        return render(request, 'accounts/html/our_profile.html', {'form': form, 'form_profile': form_profile})
    ''' if url not equals username get url and seek user that was in url'''
    user_info = UserCustom.objects.get(username=user_name)  
    return render(request, 'accounts/html/user_profiles.html', {'user': user_info})
    