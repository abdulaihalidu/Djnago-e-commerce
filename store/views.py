from django.http import JsonResponse
from django.shortcuts import redirect, render
import json
import datetime
from .models import *
from .utils import *

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CustomerForm, createUserForm

# Create your views here.


def signUpPage(request):
    form = createUserForm()
    
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Successfully created an account for ' + username + "!")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'store/register.html', context)

def logInPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            customer, _ = Customer.objects.get_or_create(name=username)
            customer.email = email
            customer.user = user
            customer.save()
    
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Username Or Password incorrect!')
    
    context = {}
    return render(request, 'store/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('store')


def store(request):
    user_is_logged = user_status(request)
    data = cartData(request)
    cartItems = data['cartItems']
    if request.user.is_authenticated:
        global customer_name
        customer_name = data['customer'].name
    else:
        customer_name = ''

    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems,
        'customer_name': customer_name,
        'user_is_logged': user_is_logged,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, product_slug):
    try:
        selected_product = Product.objects.get(slug=product_slug)
        product_available = True
        return render(request, 'store/product_details.html', {
            'product_available': product_available,
            'product': selected_product
        })
    except:
        product_available = False
        return render(request, 'store/product_details.html', {
            'product_available': product_available
        })


def cart(request):
    user_is_logged = user_status(request)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    if request.user.is_authenticated:
        customer_name = data['customer'].name
    else:
        customer_name = ''

    context = {
        'items': items,
        'order':order,
        'cartItems': cartItems,
        'user_is_logged': user_is_logged,
        'customer_name': customer_name
        }
    return render(request, 'store/cart.html', context)


def checkout(request):
    user_is_logged = user_status(request)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.user.is_authenticated:
        customer_name = data['customer'].name
    else:
        customer_name = ''

    context = {
        'items': items,
        'order':order,
        'cartItems': cartItems,
        'user_is_logged': user_is_logged,
        'customer_name': customer_name
        }
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added successfully!', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestUserOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
    return JsonResponse('payment complete.', safe=False)