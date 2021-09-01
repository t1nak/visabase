from django.shortcuts import render

# Create your views here.


def index(request):
	meetups = [{ 'title': 'First VISA', 'location':'cape Town', 'slug': 'a-first-meetup'},
	{ 'title': 'Second VISA', 'location':'johannesburg', 'slug': 'a-second-meetup'},

	]


	return render(request,'meetups/index.html',
		{'show_visas': False,
		'visas':meetups}
		)



def meetup_details(request, meetup_slug):
	print(meetup_slug)
	selected_visa = {
	'title': 'TRV',
	'description':'This is the temporary visa!'
	}
	return render(request,'meetups/meetupdetails.html',
		{'visa_title': selected_visa['title'],
		'visa_description': selected_visa['description']
		}
		)



