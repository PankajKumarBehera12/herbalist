from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.cart import Cart
# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password != password2:
            return HttpResponse("Passwords do not match")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken")
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already registered")
        
        Myuser = User.objects.create_user(username=username, password=password, email=email)
        Myuser.save()

        # print(username,password,email)
        # User creation logic here (not implemented)
        return redirect('accounts:home')  # Redirect to login page after registration (not implemented)
    return render(request, 'register.html') 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if request.user.is_authenticated:
            Cart(request)  # Initialize cart for the user
            return redirect('accounts:home')
        # Authentication logic here (not implemented)
        # Redirect to a home page after login (not implemented)
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

# @login_required
def home(request):
    products = Product.objects.all() 
    return render(request, 'home.html',  {'products': products})

