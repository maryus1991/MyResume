# Generated by Django 5.1 on 2024-08-12 12:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MyResumeSkill', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LastProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='LastProjects/')),
                ('title', models.CharField(max_length=100)),
                ('users', models.CharField(max_length=100)),
                ('Link_url', models.URLField()),
                ('description', models.TextField()),
                ('GitHub_url', models.URLField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LastProjects', to=settings.AUTH_USER_MODEL)),
                ('UserSkill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LastProjects', to='MyResumeSkill.userskill')),
                ('UserSubSkill', models.ManyToManyField(blank=True, related_name='LastProjects', to='MyResumeSkill.usersubskill')),
            ],
        ),
        migrations.CreateModel(
            name='LastProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='LastProjectGallery/')),
                ('last_projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LastProjectGallery', to='MyResumeLastProjects.lastprojects')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('last_projects', models.ManyToManyField(blank=True, null=True, related_name='ProjectCategory', to='MyResumeLastProjects.lastprojects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProjectCategory', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
