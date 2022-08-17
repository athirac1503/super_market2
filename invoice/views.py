from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request, 'user_app/user_login.html')

def sign_up(request):   
    return render(request, 'user_app/sign_up.html')

def add_product(request):
    return render(request, 'user_app/add_product.html')
def billing(request):
    return render(request,'user_app/billing.html')