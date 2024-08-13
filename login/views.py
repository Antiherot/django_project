from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        user = authenticate(username= request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')
        else:
            return render(request, 'Login.html', {})

    return render(request, 'Login.html', {})

@login_required
def logout_user(request):
        logout(request) 
        return redirect('home')


