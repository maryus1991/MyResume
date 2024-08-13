from django.db import models
from django.contrib.auth.models import User


class UserSkill(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skill')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UserSubSkill(models.Model):
    UserSkills = models.ForeignKey(UserSkill, related_name='user_skills', on_delete=models.CASCADE, null=True,
                                   blank=True)
    title = models.CharField(max_length=100)
    PercentTage = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skills')

    def __str__(self):
        return self.title


class Professional_Skills(models.Model):
    user = models.ForeignKey(User, related_name='user_Pskills', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    PercentTage = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
