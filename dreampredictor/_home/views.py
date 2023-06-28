from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib import messages

# Create your views here.


def Home(request):
    return render(request, 'index.html')


def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': LoginForm()})
    else:
        user = LoginForm(request.POST)
        if user.is_valid():
            U = User.objects.filter(
                username=request.POST['username'], password=request.POST['password'])
            if U:
                messages.success(request, "Logged successfully!")
                request.session['user'] = request.POST['username']
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials!")
                return redirect('login')
        else:
            messages.error('Fill the form correctly!')
            return redirect('login')


def Register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': RegisterForm()})
    else:
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
            request.session['user'] = request.POST['username']
            messages.success(request, 'Registered successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Fill up the form correctly!')
            return redirect('register')


def Profile(request):
    try:
        user = request.session['user']
        U = User.objects.filter(username=user).values()
        return render(request, 'profile.html', U[0])
    except:
        messages.error(request, 'Please login first!')
        return redirect('home')


def Test(request):
    return render(request, 'test.html')


def Logout(request):
    try:
        del request.session['user']
        messages.success(request, 'Logged out!')
        return redirect('home')
    except:
        messages.error(request, 'Please login first!')
        return redirect('home')
