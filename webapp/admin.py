from django.contrib import admin
from .models import ProfileImage, ProfileVideo, GalleryImage

@admin.register(ProfileImage)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'image')
	search_fields = ('id',)
	
@admin.register(ProfileVideo)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'video')
	search_fields = ('id',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')