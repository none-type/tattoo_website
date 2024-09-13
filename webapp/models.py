from django.db import models

class ProfileImage(models.Model):
	image = models.ImageField(upload_to='profile_images/', default='default.png')

class ProfileVideo(models.Model):
	video = models.FileField(upload_to='profile_videos/', blank=True, null=True)

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"

class AboutMe(models.Model):
    content = models.TextField()

    def __str__(self):
        return 'About Me Section'

class ServicesText(models.Model):
    content = models.TextField()

    def __str__(self):
        return 'Services Info'
