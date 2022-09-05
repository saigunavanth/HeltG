from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
# Create your views here.
def main(request):
	return render(request,'main/main.html')

def main1(request):
	return render(request,'main/main1.html')
def main2(request):
	return render(request,'main/main2.html')

def contactus(request):
	cform = ContactForm(request.POST)
	if request.method == "POST":
		cform = ContactForm(request.POST)
		if cform.is_valid():
			name = cform.cleaned_data['name']
			email = cform.cleaned_data['email']
			message = cform.cleaned_data['message']
			try:
				send_mail('Query',message,email,['saigunavanth11@gmail.com'],fail_silently=False)
			except BadHeaderError:
				return HttpResponse("invalid")
			return HttpResponse("suceess")
		else:
			print("error")
	return render(request,'main/contactus.html',{'cform':cform})

