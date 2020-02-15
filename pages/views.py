from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

def index(request):
	# Get last listings
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

	contex = {
		'listings': listings
	}
	print(listings)


	return render(request, 'pages/index.html', contex)

def about(request):
	# Get all realtors
	realtors = Realtor.objects.order_by('-hire_date')

	# Get MPV

	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

	context = {
		'realtors' : realtors,
		'mvp_realtors' : mvp_realtors
	}

	return render(request, 'pages/about.html', context)
