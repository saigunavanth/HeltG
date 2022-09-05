from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=100,null=True)
	email = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True,blank=True)
	image = models.ImageField(null=True,blank=True)
	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except :
			url = ''
		return url	

class Order(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100,null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	quantity = models.IntegerField(default=0,null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		return self.product.price * self.quantity

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	address = models.CharField(max_length=200,null=False)
	city = models.CharField(max_length=200,null=False)
	state = models.CharField(max_length=200,null=False)
	zipcode = models.CharField(max_length=200,null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address




class UOrder(models.Model):
	pname = models.CharField(max_length=100,null=True)
	email = models.CharField(max_length=100,null=True)
	address = models.CharField(max_length=100,null=True)
	city = models.CharField(max_length=100,null=True)
	phonenumber = models.IntegerField()
	specfications = models.CharField(max_length=100,null=True)
	price = models.FloatField()

	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.pname
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except :
			url = ''
		return url	












