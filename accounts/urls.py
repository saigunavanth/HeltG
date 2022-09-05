from django.urls import path
from accounts import views

urlpatterns = [
	path('base',views.base,name='base'),
	path('login/',views.user_login,name='login'),
	path('registration/',views.registration,name='registration'),


]