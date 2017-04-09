from django.contrib import admin
from account.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)
