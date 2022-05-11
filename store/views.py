# Create your views here.
from venv import create
from django.shortcuts import render
from matplotlib.style import context
from pytest import Item
from .models import *
from django.core.exceptions import ObjectDoesNotExist



def store(request):
    products= Product.objects.all()
    context={'products':products}
    return render(request, 'store/store.html', context)



def cart(request):
    
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitems_set.all()
        except ObjectDoesNotExist:
            items=[]
            order={'get_cart_total':0,  'get_cart_items' :0 }
        
    
    context = {'items' : items, 'order' : order}
    return render(request, 'store/cart.html', context)







def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems_set.all()
        
        
    else:
        items=[]
        order={'get_cart_total':0,  'get_cart_items' :0 }
        
       
       
       
    context = {'items' : items, 'order' : order}
    return render(request, 'store/checkout.html', context)
	

