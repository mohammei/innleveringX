from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect

def user_register(request):
    context = {}
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'useraccount/register.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            context['login_failed'] = True
    return render(request, 'useraccount/login.html', context)


# Create your views here.
