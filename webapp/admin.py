from django.contrib import admin
from .models import ProfileImage, ProfileVideo, GalleryImage, AboutMe, ServicesText

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

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('content',)  # Customize how the content is displayed in the list view

@admin.register(ServicesText)
class ServicesTextAdmin(admin.ModelAdmin):
	list_display = ('content',)
