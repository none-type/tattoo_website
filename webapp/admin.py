from django.contrib import admin
from .models import ProfileImage, ProfileVideo

@admin.register(ProfileImage)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'image')
	search_fields = ('id',)
	
@admin.register(ProfileVideo)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'video')
	search_fields = ('id',)

