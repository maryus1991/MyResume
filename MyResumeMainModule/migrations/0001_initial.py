# Generated by Django 5.1 on 2024-08-12 12:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='Profile_Image')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('short_addr', models.CharField(max_length=50)),
                ('vert_short_about', models.CharField(max_length=150)),
                ('git_url', models.URLField(blank=True, default='', null=True)),
                ('linkin_url', models.URLField(blank=True, default='', null=True)),
                ('resume_file', models.FileField(upload_to='Profile_Resume_file')),
                ('reserved_rights_text', models.CharField(max_length=50)),
                ('posts', models.BooleanField(default=False)),
                ('client_review', models.BooleanField(default=False)),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile', to='MyResumeMainModule.userprofile')),
            ],
        ),
    ]
