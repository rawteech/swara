from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from account.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile


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


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)

		if user_form.is_valid():
			# Create new user object without saving
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			# Now save the user object
			new_user.save()
			# Create the user profile
			profile = Profile.objects.create(user=new_user)

			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()

	return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
	context = dict()
	
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(
			instance=request.user.profile, 
			data=request.POST, 
			files=request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	context['user_form'] = user_form
	context['profile_form'] = profile_form
	return render(request, 'account/edit.html', context)


@login_required
def user_list(request):
	context = dict()
	template = 'account/user/list.html'

	users = User.objects.filter(is_active=True)

	context['section'] = 'people'
	context['users'] = users
	return render(request, template, context)


@login_required
def user_detail(request, username):
	context = dict()
	template = 'account/user/detail.html'

	user = get_object_or_404(User, username=username, is_active=True)

	context['section'] = 'people'
	context['user'] = user
	return render(request, template, context)
