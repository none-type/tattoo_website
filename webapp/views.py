from django.shortcuts import render
from .models import ProfileImage, ProfileVideo, GalleryImage, AboutMe, ServicesText

def index(request):
	about_me = AboutMe.objects.first()
	services_info = ServicesText.objects.first()
	profile = ProfileImage.objects.first()
	profile_video = ProfileVideo.objects.first()
	gallery_images = GalleryImage.objects.all()
	return render(request, 'index.html', {
		'services_info': services_info,
		'about_me': about_me,
		'profile': profile,
		'profile_video': profile_video,
		'gallery_images': gallery_images, 

		})
