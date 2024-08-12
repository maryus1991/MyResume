from django.contrib import admin
from .models import UserProfile, UserAbout, ContactUser
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAbout)
admin.site.register(ContactUser)

