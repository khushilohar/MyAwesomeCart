from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import *
from .models import Product, Orders
from math import ceil
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="/shop/login/")
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'msg': ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "please make sure to enter relevant search query "}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, 'shop/tracker.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html', {'product': product[0]})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(username, email, pass1, pass2)

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username Already Exist')
            return redirect('/shop/signup/')
        user = User.objects.create(
            username=username,
            email=email

        )
        user.set_password(pass1)
        user.save()
        messages.info(request, 'Account Created Successfully')

        return redirect('/shop/signup/')
    return render(request, 'shop/signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username !!')
            return redirect('/shop/login/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password !!')
            return redirect('/shop/login/')
        else:
            login(request, user)
            return redirect('/shop/')
    return render(request, 'shop/login.html')


def logoutpage(request):
    logout(request)
    return redirect('/shop/login/')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + \
                  request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email,
                       address=address, city=city, state=state,
                       zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html',
                      {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
