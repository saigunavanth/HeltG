from django.urls import path
from rental import views
urlpatterns = [
	path('rentalmain',views.main,name='rentalmain'),
	path('store',views.store,name='store'),
	path('cart',views.cart,name='cart'),
	path('checkout',views.checkout,name='checkout'),
	path('user',views.User,name='user'),
	#path('delete_order', views.deleteorder, name="delete_order"),

]