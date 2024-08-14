from django.contrib.auth import models
from django.db import models
from django.contrib.auth.models import User
from MyResumeSkill.models import UserSkill


# user profile


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    phone_number = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='Profile_Image/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    short_addr = models.CharField(max_length=50)
    vert_short_about = models.CharField(max_length=150)
    git_url = models.TextField(null=True, blank=True, default='')
    linkin_url = models.TextField(null=True, blank=True, default='')
    telegram_url = models.TextField(null=True, blank=True, default='')
    resume_file = models.FileField(upload_to='Profile_Resume_file/', null=True, blank=True)
    reserved_rights_text = models.CharField(max_length=50)
    Work_space = models.CharField(max_length=50, null=True, blank=True)
    posts = models.BooleanField(default=False)
    client_review = models.BooleanField(default=False)
    showing_exp = models.BooleanField(default=True)
    Showing_Main_Skill = models.OneToOneField(UserSkill, on_delete=models.CASCADE, related_name='UserProfile')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class UserAbout(models.Model):
    Profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='UserAbout')
    title = models.CharField(max_length=50)
    about = models.TextField()
    skill = models.ManyToManyField(UserSkill, related_name='UserAbout', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ContactUser(models.Model):
    Profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ContactUser', default=None, null=True, blank=True)
    skill = models.CharField(max_length=50, default='user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserVisit(models.Model):
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserViews')
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ip} {self.user}'
