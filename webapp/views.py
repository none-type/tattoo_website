from django.shortcuts import render
from .models import ProfileImage, ProfileVideo, GalleryImage

def index(request):
	profile = ProfileImage.objects.first()
	profile_video = ProfileVideo.objects.first()
	gallery_images = GalleryImage.objects.all()
	return render(request, 'index.html', {
		'profile': profile,
		'profile_video': profile_video,
		'gallery_images': gallery_images, 

		})
