# Generated by Django 5.1 on 2024-08-14 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyResumeMainModule', '0011_userprofile_showing_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuser',
            name='Profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ContactUser', to='MyResumeMainModule.userprofile'),
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='skill',
            field=models.CharField(default='user', max_length=50),
        ),
    ]
