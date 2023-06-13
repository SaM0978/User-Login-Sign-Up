from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import SuspiciousOperation
from home.models import UserCreation
import string

# Functions

def special_check(password):
    count = 0
    for letters in password:
        if letters in string.punctuation:
            count += 1

    if count == 0:
        return True
    else:
        return "Special Character Are Not Allowed"

def red(url):
    return redirect(url)


def length(password):
    ctr = 0
    for letters in password:
        ctr +=1

    if ctr > 17:
        return False
    elif ctr < 17:
        return True


def Pass_Check(password):
    sc = special_check(password)
    if length(password) and sc:
        return True
    else:
        if type(sc) == str:
            raise ValueError(f"{sc} Also Make Your Password Shorter Than 17")

# Create your views here.
def index(request):
        return render(request, 'index.html')


@login_required
def dashboard(request):
    user = UserCreation.objects.filter(username=request.user).first()
    print(request.user)
    if user:
        return render(request, 'dashboard.html', {"user": user})




@csrf_exempt
def signup(request):
    if request.method == "POST":
        r = request.POST
        username = r.get('username')
        email = r.get('email')
        password = r.get('password')
        if Pass_Check(password):
            user = UserCreation(username=username, email=email, password=password)
            user.save() 
            id = user.create()
            return redirect('login')
        else:
            raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")
    else:
        return render(request, 'signup.html')




@csrf_exempt
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')    
            else:
                return render(request, 'login.html')
        
        return render(request, 'login.html')
    else:
        return redirect('/')

def logoutUser(request):
    logout(request)
    return render(request, 'logout.html')