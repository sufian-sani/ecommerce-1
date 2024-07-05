from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
	print('sdhsajkdh')
	if request.user.is_authenticated:
		return HttpResponse('You are authenticated')
	else:
		form = UserCreationForm()
		if request.method == 'POST' or request.method == 'post':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse('You have successfully registered')

	context = {
		'form': form
	}

	return render(request, 'register.html',context)

def customer_login(request):
	if request.user.is_authenticated:
		return HttpResponse('You are authenticated')
	else:
		if request.method == 'POST' or request.method == 'post':
			username = request.POST.get('username')
			password = request.POST.get('password')
			customer = authenticate(request, username=username, password=password)
			if customer is not None:
				login(request, customer)
				return HttpResponse('You are logged in successfully')
			else:
				return HttpResponse('404')
	return render(request, 'login.html')
