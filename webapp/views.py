from django.shortcuts import render
from .models import ProfileImage, ProfileVideo

def index(request):
	profile = ProfileImage.objects.first()
	profile_video = ProfileVideo.objects.first()
	return render(request, 'index.html', {'profile': profile, 'profile_video': profile_video})
