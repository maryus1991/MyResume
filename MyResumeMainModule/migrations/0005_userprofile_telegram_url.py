# Generated by Django 5.1 on 2024-08-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyResumeMainModule', '0004_alter_userabout_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telegram_url',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
