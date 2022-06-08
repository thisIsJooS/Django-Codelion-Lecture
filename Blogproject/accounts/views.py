from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']
        
        user = auth.authenticate(request, username=userid, password=userpw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST['user-id']
        user.set_password(request.POST['user-pw'])
        user.save()
        return redirect('home')
    return render(request, 'signup.html')
        
        