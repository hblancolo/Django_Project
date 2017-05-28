from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    print(request.user.is_authenticated())
    title = 'Login'
    form = UserLoginForm(request.POST or None)

    if not request.user.is_authenticated():
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('music:index')
        return render(request, 'accounts/login_form.html', {'form': form, 'title': title})

    else:
        return render(request, 'accounts/already_logged_in.html', {})


def register_view(request):
    print(request.user.is_authenticated())
    title = 'Register'
    form = UserRegisterForm(request.POST or None)
    context = {'form': form, 'title': title}

    if not request.user.is_authenticated():
        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            new_user = authenticate(username=user.username,password=password)
            login(request, new_user)

            return redirect('music:index')

        return render(request, 'accounts/registration_form.html', context)

    else:
        return render(request, 'accounts/already_logged_in.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'accounts/logged_out.html', {})
    return redirect('music:index')