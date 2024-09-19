from django.db import models

class ProfileImage(models.Model):
    image = models.ImageField(upload_to='profile_images/', default='default.png')

    class Meta:
        verbose_name = "Profile Image"
        verbose_name_plural = "Profile Image"

class ProfileVideo(models.Model):
    video = models.FileField(upload_to='profile_videos/', blank=True, null=True)

    class Meta:
        verbose_name = "Profile Video"
        verbose_name_plural = "Profile Video"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title or f"Image {self.id}"

class AboutMe(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "About Me Text"
        verbose_name_plural = "About Me Text"

    def __str__(self):
        return 'About Me Section'

class ServicesText(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "Services Text"
        verbose_name_plural = "Services Text"

    def __str__(self):
        return 'Services Info'
