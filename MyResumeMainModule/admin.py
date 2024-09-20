from django.contrib import admin
from .models import UserProfile, UserAbout, ContactUser, UserVisit
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAbout)
admin.site.register(ContactUser)


@admin.register(UserVisit)
class UserVisitAdmin(admin.ModelAdmin):
    list_display = ('ip', 'created_at',)

