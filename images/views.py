from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from images.forms import ImageCreateForm
from images.models import Image


@login_required
def image_create(request):
	context = dict()

	if request.method == 'POST':
		form = ImageCreateForm(data=request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			new_item = form.save(commit=False)

			# assign current user to item
			new_item.user = request.user
			new_item.save()
			messages.success(request, 'Your image has been added successfully')

			# redirect to the item's detail view
			return redirect(new_item.get_absolute_url())

	else:
		# build form with GET data provided by bookmarklet
		form = ImageCreateForm(data=request.GET)

	context['section'] = 'images'
	context['form'] = form
	return render(request, 'images/image/create.html', context)


def image_detail(request, id, slug):
	context = dict()
	image = get_object_or_404(Image, id=id, slug=slug)

	context['section'] = 'images'
	context['image'] = image
	return render(request, 'images/image/detail.html', context)
