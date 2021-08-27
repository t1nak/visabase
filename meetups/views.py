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



