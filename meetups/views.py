from django.shortcuts import render

# Create your views here.
from .models import Visa

def index(request):
	meetups = Visa.objects.all()

	return render(request,'meetups/index.html',
		{
		'visas':meetups}
		)



def meetup_details(request, meetup_slug):
 	
 	try:
 		selected_visa =  Visa.objects.get(slug=meetup_slug)
 		return render(request,'meetups/meetup_details.html',
			{
			'visa_found': True,
			'visa_title': selected_visa.title,
			'visa_description': selected_visa.description
			}
			)
 	except Exception as exc:
 		return render(request,'meetups/meetup_details.html',
			{'visa_title': selected_visa.title,
			'visa_found': False,
			'visa_description': selected_visa.description
			}
			)		




