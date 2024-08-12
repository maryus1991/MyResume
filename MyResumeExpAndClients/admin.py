from django.contrib import admin
from .models import WorkExpt, StudyExpt, UserPosts, UserClientReview, WorkExptResponsibility
# Register your models here.

admin.site.register(WorkExpt)
admin.site.register(StudyExpt)
admin.site.register(UserPosts)
admin.site.register(UserClientReview)
admin.site.register(WorkExptResponsibility)
