from django.db import models
from django.contrib.auth.models import User


class StudyExpt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_expts')
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    url_name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class WorkExpt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_expts')
    from_date = models.DateField()
    to_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    work_space = models.CharField(max_length=100, blank=True, null=True)
    responds_1 = models.CharField(max_length=100, blank=True, null=True)
    responds_2 = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.title


# class WorkExptResponsibility(models.Model):
#     work = models.ForeignKey(WorkExpt, on_delete=models.CASCADE, related_name='responsibilities')
#     title = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     is_deleted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title


class UserPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserPosts')
    title = models.CharField(max_length=100)
    description = models.TextField()
    url_name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UserClientReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserClientReviews')
    image = models.ImageField(upload_to='Client_images/')
    author = models.CharField(max_length=100)
    description = models.TextField()
    author_ability = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.author
