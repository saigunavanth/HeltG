from django.shortcuts import render
from .forms import *
from .models import *
from .filters import *
# Create your views here.
def main(request):
	products = UOrder.objects.all()
	context = {'products':products}
	return render(request,"rental/main.html",context)

def store(request):
	products = UOrder.objects.all()
	context = {'products':products}
	return render(request,"rental/store.html",context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {"get_cart_total":0,"get_cart_items":0}
	context = {"items":items,'order':order}
	return render(request,"rental/cart.html",context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {"get_cart_total":0,"get_cart_items":0}
	context = {"items":items,'order':order}
	return render(request,"rental/checkout.html",context)

def User(request):
	if request.method == "POST":
		form = UserOrderInfo(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			
	else:
		form = UserOrderInfo()

	products = UOrder.objects.all()
	context = {'products':products,'form':UserOrderInfo}
	return render(request,'rental/user.html',context)

# def deleteorder(request,*args,**kwargs):
# 	pk = kwargs.get('pk')
# 	print(pk)
# 	order = UOrder.objects.get(id=pk)
# 	print(order)
# 	if request.method=="POST":
# 		order.delete()
# 	return render(request,"rental/delete.html",{"order":order})
