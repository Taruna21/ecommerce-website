# Create your views here.
from venv import create
from django.shortcuts import render
from matplotlib.style import context
from pytest import Item
from .models import *




def store(request):
    products= Product.objects.all()
    context={'products':products}
    return render(request, 'store/store.html', context)



def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.custmer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems_set.all()
        
    else:
        items=[]
    
    context = {'items' : items}
    return render(request, 'store/cart.html', context)





def checkout(request):
	context={}
	return render(request, 'store/checkout.html', context)

