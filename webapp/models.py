from django.db import models

class ProfileImage(models.Model):
	image = models.ImageField(upload_to='profile_images/', default='default.png')

class ProfileVideo(models.Model):
	video = models.FileField(upload_to='profile_videos/', blank=True, null=True)