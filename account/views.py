from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from account.forms import LoginForm


# def user_login(request):
# 	context = dict()

# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)

# 		# Validate form data
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			user = authenticate(username=cd['username'], password=cd['password'])

# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
# 					return HttpResponse('Authenticated Successfully')

# 				else:
# 					return HttpResponse('Disabled account')

# 			else:
# 				return HttpResponse('Invalid Login')

# 	else:
# 		form = LoginForm()

# 	context['form'] = form
# 	return render(request, 'account/login.html', context)

@login_required
def dashboard(request):
	context = dict()

	context['section'] = 'dashboard'
	return render(request, 'account/dashboard.html', context)
