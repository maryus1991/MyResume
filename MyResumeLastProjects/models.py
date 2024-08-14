from django.db import models
from django.contrib.auth.models import User
from MyResumeSkill.models import UserSkill, UserSubSkill


# Create your models here.


class LastProjects(models.Model):
    image = models.ImageField(upload_to='LastProjects/')
    title = models.CharField(max_length=100)
    UserSubSkill = models.ManyToManyField(UserSubSkill, null=True, blank=True, related_name='LastProject')
    OtherSubSkill = models.CharField(max_length=100, null=True, blank=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='LastProjects')
    UserSkill = models.ForeignKey(UserSkill, on_delete=models.CASCADE, related_name='LastProject')
    Link_url = models.URLField(max_length=200)
    description = models.TextField()
    GitHub_url = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_project_sub_skill(self):
        return self.UserSubSkill.all()


class LastProjectGallery(models.Model):
    image = models.ImageField(upload_to='LastProjectGallery/')
    last_projects = models.ForeignKey(LastProjects, on_delete=models.CASCADE, related_name='LastProjectGallery')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.last_projects.title


class ProjectCategory(models.Model):
    title = models.CharField(max_length=100)
    last_projects = models.ManyToManyField(LastProjects, related_name='ProjectCategory',
                                           blank=True,
                                           null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ProjectCategory')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
