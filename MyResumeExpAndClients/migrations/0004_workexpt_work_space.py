# Generated by Django 5.1 on 2024-08-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyResumeExpAndClients', '0003_alter_workexpt_from_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexpt',
            name='work_space',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
