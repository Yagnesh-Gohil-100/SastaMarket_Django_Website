from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductImage, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    # products = ProductImage.objects.all()
    products = Product.objects.prefetch_related('images')
    return render(request, 'home.html', {'products':products})

# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'home.html', {'product': product})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in...")
            return redirect('home')
        else:
            messages.success(request, "whoops! An error has been occured during login, Please try again...")
            return redirect('login')
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Thank you for registering at Sasta Market... You can now start buying at affordable price!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, Please try again...")
            return redirect('register')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

